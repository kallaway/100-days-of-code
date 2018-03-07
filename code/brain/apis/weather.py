import requests
from config import config
from log import logger
import simplejson as json
_TORONTO_LOCATION_ID = 55488

def get_real_feel_temp_in_celcius():
  """

  :return:
  """
  try:
    resp = requests.get('http://dataservice.accuweather.com/currentconditions/v1/{}'.format(_TORONTO_LOCATION_ID),
      params = {
        'apikey': config['APIS']['ACCUWEATHER'],
        'details': 'true'
    })
    resp.raise_for_status()
    data = resp.json()
    logger.debug('Weather response {}'.format(json.dumps(data, indent = 4)))
    return data[0].get('RealFeelTemperature').get('Metric').get('Value'), None
  except requests.exceptions.RequestException as e:
    logger.exception('error fetching weather')
    return None, Exception('Can\'t fetch weather')

