from game_data import data
import random
from art import logo, vs
# from replit import clear

# pick a random entry from data
def random_selection():
  return random.choice(data) 

# setup display results
def display_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]

  return f"{name} is a {description} from {country}"

# This function will be called in start_game, and checks if user
# guess matches correct answer
def check_answer(guess, match1_followers, match2_followers):
  if match1_followers > match2_followers:
    return guess == "a"
  else:
    return guess == "b"
 
 # define game functionality
def start_game():
  print(logo)
  score = 0
  game_continue = True
  match1 = random_selection()
  match2 = random_selection()

  while game_continue:
    match1 = match2
    match2 = random_selection()

    if match1 == match2:
      match2 = random_selection()

    print(f"Compare A: {display_data(match1)}.")
    print(vs)
    print(f"Compare B: {display_data(match2)}.")

    guess = input("Who do you think has more followers? Type 'A' or 'B': ").lower()
    match1_follower_count = match1["follower_count"]
    match2_follower_count = match2["follower_count"]
    is_correct = check_answer(guess, match1_follower_count, match2_follower_count)

    # clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

start_game()