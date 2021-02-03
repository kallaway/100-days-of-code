#Step 1 
import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_game = False
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
lives = 6
# guessed_letters = []
display = []
wordlength = len(chosen_word)

for _ in range(wordlength):
  display += "_"
print(display)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.



while not end_game:
  guess = input("Guess a letter: ").lower()

  # print(guess)
  # print(guessed_letters)

  #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  for position in range(wordlength):
    letter = chosen_word[position]
    print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    
    if letter == guess:
        display[position] = letter

  if guess not in chosen_word:
    lives -=1
    if lives == 0:
      end_game = True
      print("You lose.")


  print(f"{' '.join(display)}")

  print(display)

  if "_" not in display:
    end_game = True
    print("You Win!")

  print(stages[lives])
