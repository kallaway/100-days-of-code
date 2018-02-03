from config import config
from fbmq import Page
from log import logger

page = Page(config['FACEBOOK']['PAGE_TOKEN'])
page.greeting("Welcome!")



@page.handle_message
def message_handler(event):
  """:type event: fbmq.Event"""
  sender_id = event.sender_id
  recipient_id = event.recipient_id
  time_of_message = event.timestamp
  message = event.message

  logger.info("Received message for user %s and page %s at %s with message:"
               % (sender_id, recipient_id, time_of_message))
  logger.info(message)
  try:
    page.send(sender_id, "🙏 ! I was born like yesterday 👶. So still learning how to interact" % message)
    return None
  except Exception as e:
    return Exception('could not send message sender_id={} recipient_id={} time_of_message={}'.format(sender_id,
                                                                                                     recipient_id,
                                                                                                     time_of_message))

