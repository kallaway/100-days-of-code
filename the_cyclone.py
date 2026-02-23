# Write code below 💖

height= float(input('Whats your height?'))
credits=float(input('How many credits do you have?'))

if height>137 and credits>10:
  print('Enjoy the ride!')
elif credits>10 and height <137:
  print('You are not tall enough')
elif height>137 and credits<10:
  print('You dont have enough credits')
else:
  print('You are not allowed!!')