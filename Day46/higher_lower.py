# import logo from art file
from art import logo, vs

# import the data file
from game_data import data

# import random
import random

# pick a random entry from data
def random_selection():
  print(random.choice(data)) 

# setup display results
def display_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]

  return f"{name} is a {description} from {country}"

def check_answer(guess, a_followers, b_followers):
  """Check followers against user's guess 
  and returns True if they get it right.
  Or False if they get it wrong.""" 
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

    print(f"Compare A: {display_data(match1)}")
    print(vs)
    print(f"Compare B: {display_data(match2)}")

    guess = input("Who do you think has more followers? Type 'A' or 'B': ").lower()