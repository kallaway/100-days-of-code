# This is just practicing scraping the PGA tour site.

import urllib2
from bs4 import BeautifulSoup
import pandas as pd

players_url = "https://www.pgatour.com/players.html"
page = urllib2.urlopen(players_url)
soup = BeautifulSoup(page, 'html.parser')
#players_list = soup.find_all('ul', attrs={'class':'items'})
players = soup.find_all('li', attrs={'class':'player-card'})
for player in players:
  first_name = player.find('span', attrs={'class':'player-firstname'})
  last_name = player.find('span', attrs={'class':'player-surname'})
  country = player.find('div', attrs={'class':'player-country-title'})
  url = player.find('a', attrs={'class':'player-link'}, href=True)
  print first_name.text, last_name.text, country.text, url['href']

