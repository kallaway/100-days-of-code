from flask import Flask, jsonify, make_response, request
import configparser
from github import Github
import base64
from datetime import date
from fbmq import Page
import logging

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('config.ini')
git = Github(config['GITHUB']['USER'], config['GITHUB']['PASSWORD'])
page = Page(config['FACEBOOK']['PAGE_TOKEN'])


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


@page.handle_message
def message_handler(event):
  """:type event: fbmq.Event"""
  sender_id = event.sender_id
  recipient_id = event.recipient_id
  time_of_message = event.timestamp
  message = event.message

  logging.info("Received message for user %s and page %s at %s with message:"
               % (sender_id, recipient_id, time_of_message))
  logging.info(message)
  page.send(sender_id, "🙏 ! I was born like yesterday 👶. So still learning how to interact" % message)



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
