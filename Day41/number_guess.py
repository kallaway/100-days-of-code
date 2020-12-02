print("Welcome to my number guessing game!")
print("I'm thinking of a number between 1 and 100.")

from random import randint

guesses = 10;

# if easy chosen, they have 10 guesses, otherwise 7
difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")
if difficulty == "hard":
    guesses = 7;
    print(f"You have {guesses} guesses remaining.")
        
else:
    print(f"You have {guesses} guesses remaining")
    # make a guess
# compare guess with selected random number. If guess higher, print too high, else too low.
random = randint(1, 100)
print(random)
guess = int(input("Guess a number "))
print(guess)
# def guess_number():
    # while guess > 0:
if guess > random:
    print("Too high.")
    print("Guess again.")
    guesses = guesses - 1
    print(f"You have {guesses} guesses left.")
elif guess < random: 
    print("Too low.")
    print("Guess again.")
    guesses = guesses - 1
    print(f"You have {guesses} guesses left.")
else:
    print("You got it!")

# guess_number()




