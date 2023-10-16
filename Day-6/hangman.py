import os
import requests


def main():
    gameword = getword()
    rungame(gameword)


def getword():
    return requests.get('https://random-word-api.herokuapp.com/word').json()[0]


def rungame(gameword):
    gamewordlength = len(gameword)
    allletters = list(gameword)
    gameout = ['_'] * gamewordlength
    gamestate = 0
    guesses = []

    while gamestate < 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        gallows(gamestate)
        print(f'Your word has {gamewordlength} letters.')
        print('This is your word: ' , *gameout)
        print('Letters you have guessed: ' , *guesses)
        guess = input("Please enter your guess: ").lower()[0]
        guesses.append(guess)

        changed = False
        for i,v in enumerate(allletters):
            if guess == v:
                changed = True
                gameout[i] = v
                print(*gameout)
        
        if changed == False:
            gamestate += 1
            print(*gameout)

        if "_" not in gameout:
            gallows(gamestate)
            print("You Win")
            exit()
    print(f'Unfortunately you lose.  Your word was {gameword}')




def gallows(gs):
    drawing=[
       """  ===|
      |
      |
      |
    __|__ """,
    """  ===|
      |  O
      |
      |
    __|_""",
    """  ===|
      |  O
      |  |
      |  |
    __|_""",
    """  ===|
      |  O
      | /|
      |  |
    __|_""",
    """  ===|
      |  O
      | /|\\
      |  |
    __|_""",
    """  ===|
      |  O
      | /|\\
      |  |
    __|_/""",
    """  ===|
      |  O
      | /|\\
      |  |
    __|_/ \\"""]
    print(drawing[gs])


if __name__ == '__main__':
    main()
