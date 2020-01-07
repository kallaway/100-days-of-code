# This is just practicing scraping the PGA tour site.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def get_soup_from_url(url):
    page = urlopen(url)
    return BeautifulSoup(page, 'html.parser')

def get_players_list(print_list=False):
    """ scrapes the site for a full list of players.

    Parameters
    ----------
    print_list : bool, optional
        A flag to print out the list of players (default is False)
    
    Returns
    -------
    """
    
    players_url = "https://www.pgatour.com/players.html"
    soup = get_soup_from_url(players_url)
    players = soup.find_all('li', attrs={'class':'player-card'})
    for player in players:
        first_name = player.find('span', attrs={'class':'player-firstname'})
        last_name = player.find('span', attrs={'class':'player-surname'})
        country = player.find('div', attrs={'class':'player-country-title'})
        url = player.find('a', attrs={'class':'player-link'}, href=True)
        if print_list:
            print(first_name.text, last_name.text, country.text, url['href'])


def main():
    get_players_list(True)

if __name__ == "__main__":
    main()
