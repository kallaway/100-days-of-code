from flask import Flask, jsonify, make_response, request
import base64
from datetime import date, datetime, timedelta
from pytz import timezone
from log import logger
from github import Github
from config import config
from fbmessenger import page
from apis.weather import get_real_feel_temp_in_celcius

app = Flask(__name__)
git = Github(config['GITHUB']['USER'], config['GITHUB']['PASSWORD'])
_TIMEZONE = 'US/Eastern'
_MY_RECIPIENR_ID = 1559656084121864

@app.route('/fb/webhook', methods=['GET'])
def validate():
  if request.args.get('hub.mode', '') == 'subscribe' and \
                  request.args.get('hub.verify_token', '') == config['FACEBOOK']['VERIFY_TOKEN']:

    logger.debug("Validating webhook")

    return request.args.get('hub.challenge', '')
  else:
    return 'Failed validation. Make sure the validation tokens match.'

@app.route('/fb/webhook', methods=['POST'])
def webhook():
  payload = request.get_data(as_text=True)
  logger.debug("webhook payload: {}".format(payload))
  page.handle_webhook(payload)
  return "ok"

@app.errorhandler(400)
def not_found(error):
  return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def root():
  return jsonify({'message': 'This is brain\'s internal server api'})

def has_todays_update(logs, date_str):
  assert logs
  today_str = date_str or datetime.now(timezone(_TIMEZONE)).strftime('%b %d, %Y')
  return today_str in logs

def is_progress_updated(today_str):
  repo = git.get_user().get_repo('100-days-of-code')
  progress_logs_file = repo.get_file_contents('log.md')
  progress_logs = str(base64.standard_b64decode(progress_logs_file.content).decode('utf-8'))
  return has_todays_update(progress_logs, today_str)

@app.route('/brain/api/v1.0/logs/is_updated_today/', defaults={
  'today_str': datetime.now(timezone(_TIMEZONE)).date().strftime('%b %d, %Y')})
@app.route('/brain/api/v1.0/logs/is_updated_today/<today_str>', methods=['GET'])
def get_logs(today_str):
  return jsonify({'result': is_progress_updated(today_str),
                  'today': today_str})

def send_no_progress_update_notification():

  try:
    today = datetime.now(timezone(_TIMEZONE)).date()
    today_str = today.strftime('%b %d, %Y')
    tomorrow = today + timedelta(days=1)
    time_until_eod = (datetime.combine(tomorrow, datetime.min.time()).replace(tzinfo=timezone(_TIMEZONE)) \
                      - datetime.now(timezone(_TIMEZONE)))
    hrs_til_eod = time_until_eod.seconds//3600
    logger.info('Datetime problem {}'.format(today, tomorrow, time_until_eod))
    if not is_progress_updated(today_str):
      page.send(_MY_RECIPIENR_ID, "No progress update for #100DaysOfCode Challenge yet! 😰~{time_left} hrs left".format(
          time_left=hrs_til_eod
      ))
      if hrs_til_eod < 2:
        page.send(_MY_RECIPIENR_ID, "Hurry Up")
    return "ok"
  except Exception as e:
    logger.exception('Couldnt send message')
    return "not ok"


def send_morning_weather_update():
  temp = get_real_feel_temp_in_celcius()[0]
  try:
    assert isinstance(temp, float)
    if temp < -10 or temp > 0:
      page.send(_MY_RECIPIENR_ID, "It feels like {} outside".format(temp))
      return "weather_report_sent"
    return "no_weather_report_sent"
  except:
    page.send(_MY_RECIPIENR_ID, "Sorry Couldn't get weather for you. #Fail")
    return "weather_report_failure_message_sent"



if __name__ == '__main__':
  app.run(debug=True, threaded=True)
