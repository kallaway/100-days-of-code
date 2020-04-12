toopings = ""
while toopings.lower() != 'quit':
     toopings = input('Enter toppings for your pizza: ')
     if toopings.lower() != 'quit':
         print(f' Adding {toopings}... ')
print('Pizza is ready')