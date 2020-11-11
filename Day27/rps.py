import random

random_user = random.randint(0, 2)
random_computer = random.randint(3,5)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
if random_user == 0:
  print("You chose rock: " + rock)
elif random_user == 1:
  print("You chose paper: " + paper)
elif random_user == 2:
  print("You chose scissors: " + scissors)
else: 
    print(" ")


if random_computer == 3:
  print("The computer chose paper: " + paper)
elif random_computer == 4:
  print("The computer chose rock: " + rock) 
elif random_computer == 5:
  print("The computer chose scissors: " + scissors)
else: 
  print(" ")


# for user = 0
if (random_user == 0) and (random_computer == 3):
  print ("You lose. Paper covers rock.")
elif (random_user == 0) and (random_computer == 4):
  print("Tie! You both chose rock.")    
elif (random_user == 0) and (random_computer == 5):
  print("You win! Rock crushes scissors.")

# for user = 1
elif (random_user == 1) and (random_computer == 3):
  print ("Tie! You both chose paper.")
elif (random_user == 1) and (random_computer == 4):
  print("You win!. Paper covers rock")    
elif (random_user == 1) and (random_computer == 5):
  print("You lose. Scissors cut paper.")

# for user = 2
elif (random_user == 2) and (random_computer == 3):
  print ("You win! Scissors cut paper.")
elif (random_user == 2) and (random_computer == 4):
  print("You lose. Rock crushes scissors.")    
elif (random_user == 2) and (random_computer == 5):
  print("Tie! You both chose scissors.")
else:
    print(" ")