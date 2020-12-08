for number in range(1, 101):
    # has to be and not or
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
    # why is it printing the number and text?
  else:
    print(number)