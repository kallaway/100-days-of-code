from flask import Flask, jsonify, make_response, request
import simplejson as json
import base64
from datetime import date
import logging
from github import Github
from config import config
from fbmessenger import page

app = Flask(__name__)
git = Github(config['GITHUB']['USER'], config['GITHUB']['PASSWORD'])


@app.route('/fb/webhook', methods=['GET'])
def validate():
  if request.args.get('hub.mode', '') == 'subscribe' and \
                  request.args.get('hub.verify_token', '') == config['FACEBOOK']['VERIFY_TOKEN']:

    logging.debug("Validating webhook")

    return request.args.get('hub.challenge', '')
  else:
    return 'Failed validation. Make sure the validation tokens match.'

@app.route('/fb/webhook', methods=['POST'])
def webhook():
  payload = request.get_data(as_text=True)
  logging.debug("webhook payload: {}".format(payload))
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

def has_todays_update(logs):
  assert logs
  today_str = date.today().strftime('%b %d, %Y')
  return today_str in logs

@app.route('/brain/api/v1.0/logs/is_updated_today', methods=['GET'])
def get_logs():
  repo = git.get_user().get_repo('100-days-of-code')
  progress_logs_file = repo.get_file_contents('log.md')
  progress_logs = str(base64.standard_b64decode(progress_logs_file.content).decode('utf-8'))
  return jsonify({'result': has_todays_update(progress_logs)})


if __name__ == '__main__':
  app.run(debug=True, threaded=True)
