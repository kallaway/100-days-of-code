#Day 7: Dictionaries and the SWOT Analysis
input()

print("The SWOT Analysis (acronym for Strengths, Weaknesses, Opportunities, and Threats) is a tool to evaluate what we are good at, bad at, can do well, and can do poorly. A common strategy for using the SWOT analysis is to design strategies to utilize our strengths and opportunities, while turning our weaknesses and threats into strengths and opportunities.")

print('              __________              __________              __________              __________')
print('             (          )            (          )            (          )            (          )')
print('             (          )            (          )            (          )            (          )')
print('             (    S     )            (    W     )            (     O    )            (     T    )')
print('             (          )            (          )            (          )            (          )')
print('             (__________)            (__________)            (__________)            (__________)')
print('               +++   ^                    |                    +++   ^                     |')
print('                     |____________________|                          |_____________________|')

strengths = []
strengths_open = 'O'
weaknesses = []
weaknesses_open = 'O'
opportunities = []
opportunities_open = 'O'
threats = []
threats_open = 'O'
print(" ")
print("Please think about some of your strengths. Enter them one by one.")                                  #enter your strengths
while strengths_open == 'O':
    
    enter = input("Please tell me one your strengths or press 'C' to close the strengths module.")
    if enter == 'C':
        strengths_open = 'C'
    if enter != 'C':
        strengths.append(enter)
      
while weaknesses_open == 'O':
    
    enter = input("Please tell me one your weaknesses or press 'C' to close the weaknesses module.")        #enter your weaknesses       
    if enter == 'C':
        weaknesses_open = 'C'
    if enter != 'C':
        weaknesses.append(enter)

while opportunities_open == 'O':
    
    enter = input("Please tell me one your opportunities or press 'C' to close the opportunities module.")  #enter your opportunities
    if enter == 'C':
        opportunities_open = 'C'
    if enter != 'C':
        opportunities.append(enter)

while threats_open == 'O':
    
    enter = input("Please tell me one your threats or press 'C' to close the threats module.")              #enter your threats
    if enter == 'C':
        threats_open = 'C'
    if enter != 'C':
        threats.append(enter)
S = len(strengths)
W = len(weaknesses)
O = len(opportunities)
T = len(threats)

print('You have ' + str(S) + ' strengths. Here is the list: ' + ' ,'.join(strengths))                       #takes out quotes 
print('You have ' + str(W) + ' weaknesses. Here is the list: ' + ' ,'.join(weaknesses))                     #in the string
print('You have ' + str(O) + ' opportunities. Here is the list: ' + ' ,'.join(opportunities))
print('You have ' + str(T) + ' threats. Here is the list: ' + ' ,'.join(threats))
      
input()
