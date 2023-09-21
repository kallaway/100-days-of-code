import os
import random


def main():
    choices = [
        'r','r','r','r','r'
        'p','p','p','p','p',
        's','s','s','s','s'
    ]
    clearscreen()
    print('Welcome to Rock Paper Scissors')
    playerchoice = input('Please select one of the following: "rock", "Paper", or "Scissors" ').lower()
    computerchoice = random.choice(choices)
    result = buildresult(playerchoice, computerchoice)
    printout, wld = gamestate(result)
    print(f'{printout} - as a result you {wld}')
    playagain = input('Do you want to play again? Yes or No: ')
    if playagain in ('y', 'yes'):
        main()
    quit()



def buildresult(playerchoice, computerchoice):
    if playerchoice in ('rock', 'r'):
        return playerchoice[0] + computerchoice
    elif playerchoice in ('paper', 'p'):
        return playerchoice[0] + computerchoice
    elif playerchoice in ('scissors', 's'):
        return playerchoice[0] + computerchoice
    else:
        print(f'You picked {playerchoice} which is not rock, paper or scissors. You fail for not following directions')
        quit()


def gamestate(gs):
    config = {
        'rr': {
            'out': 'We both played rock.',
            'winlosetie': 'draw'},
        'rp': {
            'out': 'You played rock but I played paper.',
            'winlosetie': 'lose'},
        'rs': {
            'out': 'You played rock and I played scisors.',
            'winlosetie': 'win'},
        'pr': {
            'out': 'You played paper and I played rock.',
            'winlosetie': 'win'},
        'pp': {
            'out': 'We both played paper',
            'winlosetie': 'draw'},
        'ps': {
            'out': 'You played paper but I played scissors.',
            'winlosetie': 'lose'},
        'sr': {
            'out': 'You played scissors, but I played rock',
            'winlosetie': 'lose'},
        'sp': {
            'out': 'You played scissors, and I played paper.',
            'winlosetie': 'win'},
        'ss': {
            'out': 'We both played scissors',
            'winlosetie': 'draw'
            }
    }

    result = config[gs]
    printout = result['out']
    wld = result['winlosetie']
    return printout, wld


def clearscreen():
    if os.name == 'posix':
        os.system('clear')
        return True
    elif os.name == 'nt':
        os.system('cls')
        return True
    else:
        return True


if __name__ == '__main__':
    main()
