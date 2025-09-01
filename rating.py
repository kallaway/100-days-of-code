# Write code below 💖

rating=0.0
rating=float(input('Add you ratings: '))

if rating > 4.5:
  print("Extraordinary")
elif rating>4:
  print('Excellent')
elif rating >3 and rating<=4:
  print('Good')
elif rating > 2 and rating<=3:
  print('Fair')
else:
  print('Poor')
