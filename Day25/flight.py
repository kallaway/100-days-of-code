print("Welcome to My Flight Simulator")

print(''' |
                                      --====|====--
                                            |  

                                        .-"""""-. 
                                      .'_________'. 
                                     /_/_|__|__|_\_\
                                    ;'-._       _.-';
               ,--------------------|    `-. .-'    |--------------------,
                ``""--..__    ___   ;       '       ;   ___    __..--""``
                 jgs      `"-// \\.._\             /_..// \\-"`
                             \\_//    '._       _.'    \\_//
                              `"`        ``---``        `"`''')


begin = input("Where do you want to fly from? Phoenix, Chicago, or Dallas?\n")

where_to = input("Where would you like to fly to? New York, New Jersey, or New Zealand?\n")

speed = input("How fast would you like to travel (kph)? 300, 400, 500?\n")

# options from phoenix
if (begin == "Phoenix") and (where_to == "New York"):
  distance = 2414
elif (begin == "Phoenix") and (where_to == "New Jersey"):
  distance = 2456
elif (begin == "Phoenix") and (where_to == "New Zealand"):
  distance = 6953

# options from Chicago
elif (begin == "Chicago") and (where_to == "New York"):
  distance = 791
elif (begin == "Chicago") and (where_to == "New Jersey"):
  distance = 783
elif (begin == "Chicago") and (where_to == "New Zealand"):
  distance = 8374

# options from Dallas
elif (begin == "Dallas") and (where_to == "New York"):
  distance = 1373
elif (begin == "Dallas") and (where_to == "New Jersey"):
  distance = 1340
elif (begin == "Dallas") and (where_to == "New Zealand"):
  distance = 7610
else: 
  distance = 1000

# in hours
time = round(distance / int(speed),2)

# convert to minutes


print(f"It will take you about {time} hours to get from {begin} to {where_to} at {speed} knots")