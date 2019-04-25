#Day 8: Planets of the Solar System
#Data from: https://theplanets.org/planets/

print("Planets of the Solar System:")   #'key': 'value'
print("     Mercury     Venus     Earth     Mars     Jupiter     Saturn       Uranus      Neptune")
planets = {'Mercury': {'diameter': '4,879 km', 'distance from the sun': '57,910,000 km','year': '88 days', 'moons': '0',},
           'Venus': {'diameter': '12,104 km', 'distance from the sun': '108,200,000 km', 'year': '243 days', 'moons': '0',},
           'Earth': {'diameter': '12,756 km', 'distance from the sun': '149,600,000 km', 'year': '365 days', 'moons': '1'},
           'Mars': {'diameter': '6,805 km', 'distance from the sun': '227,940,000 km', 'year': '687 days', 'moons': '2'},
           'Jupiter': {'diameter': '142,984 km', 'distance from the sun': '778,330,000 km', 'year': '4,329 days', 'moons': '67'},
           'Saturn': {'diameter': '120,536 km', 'distance from the sun': '1,424,600,000 km', 'year': '10,731 days', 'moons': '150'},
           'Uranus': {'diameter': '51,118 km', 'distance from the sun': '2,873,550,000 km', 'year': '30,770 days', 'moons': '27'},
           'Neptune': {'diameter': '49,528 km', 'distance from the sun': '4,501,000,000 km', 'year': '60,152 days', 'moons': '14'}}

query = input("\nTell me which planet you are interested in learning about.")

print(query)                            #name of planet   

print('\n' + query + ' has a diameter of ' + str(planets[query]['diameter']) +
      '.'  + ' It is ' + str(planets[query]['distance from the sun']) + ' from the Sun. ' +
      'A year on ' + query + ' is ' + str(planets[query]['year']) + ' long. ' +
      query + ' has ' + str(planets[query]['moons']) + ' moons.')
