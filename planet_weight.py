# Write code below 💖

weight= float(input('Enter your weight on earth: '))
planet= int(input(''' Enter the planet number: 1. Mercury
                      2. Venus
                      3. Mars
                      4. Jupiter
                      5. Saturn
                      6. Uranus
                      7. Neptune''' ))

if planet == 1 :
  weight = weight * 0.38
  print(weight)
elif planet == 2 :
  weight = weight * 0.91
  print(weight)
elif planet == 3 :
  weight = weight * 0.38
  print(weight)
elif planet == 4 :
  weight = weight * 2.53
  print(weight)
elif planet == 5 :
  weight = weight * 1.07
  print(weight)
elif planet == 6 :
  weight = weight * 0.89
  print(weight)
elif planet == 7 :
  weight = weight * 1.14
  print(weight)
else:
  print('Invalid Planet number')
  