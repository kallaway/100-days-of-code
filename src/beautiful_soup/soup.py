from bs4 import BeautifulSoup
import requests
from pushover import init, Client

# define the pushover client keys and tokens
client = Client("uGCmFNL2ToDycU5qL5qKNmqEadQVW8", api_token="ae5k98ek8o4mjnz7fvqaqgdfdpwsp9")

def getGoalsLeaders():
    url="https://www.hockey-reference.com/leagues/NHL_2020_leaders.html"
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html5lib')

    # grab the div containing the goals leaders rows
    goalsLeadersDiv = soup.findAll('div', attrs = {'id': 'leaders_goals'})

    leaders_list = []   # create empty list to store each leader dict in

    # loop through and grab a list of all <tr>'s in the div containing table of leaders
    for goalsLeaders in goalsLeadersDiv:
        goalsLeaders = goalsLeaders.findAll('tr',{'class':['first_place','']})
        i = 1   # to fix blank ranks, increment for each leader and set rank if blank
        # loop through each <tr> and grab each individual leader
        for leader in goalsLeaders:
            leaders_dict = {}   # create empty dict to hold stats for each leader
            # set rank and remove the '.' from the rank
            rank = leader.find('td').text.replace('.','')
            if rank == '':  # if rank is blank, set it to the string value of i
                rank = str(i)

            # scrape the name, team, and goals vars based on td and span classes
            name = leader.find('td',{'class':'who'}).a.text.strip()
            team = leader.find('span',{'class':'desc'}).text.strip()
            goals = leader.find('td',{'class':'value'}).text.strip()

            # set the keys of the leaders dict for current leader
            leaders_dict['rank'] = rank
            leaders_dict['name'] = name
            leaders_dict['team'] = team
            leaders_dict['goals'] = goals

            # append the newly created leaders_dict to leaders_list
            leaders_list.append(leaders_dict)

            i += 1  # increment the rank

    # return the value of leaders_list
    return leaders_list

def printGoalsLeaders():
    leaders_list = getGoalsLeaders()

    leaders_string = ''
    for r, n, t, g in [x.items() for x in leaders_list]:
        for k,v in r,n,t,g:
            leaders_string += v + '\t'
        leaders_string += '\n'

    print(leaders_string)
    client.send_message(leaders_string, title="Goals Leaders")

printGoalsLeaders()