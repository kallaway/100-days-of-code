import os
import random


def main():
    clearscreen()
    print('Welcome to Rock Paper Scissors')
    playerchoice = input('Please select one of the following: "rock", "Paper", "Scissors", "Lizard", or "Spock" ').lower()
    computerchoice = random.choice(['r','s','p','l','k'])
    result = buildresult(playerchoice, computerchoice)
    printout, wld = gamestate(result)
    print(f'{printout} - as a result you {wld}')
    playagain = input('Do you want to play again? Yes or No: ')
    if playagain in ('y', 'yes'):
        main()
    quit()



def buildresult(playerchoice, computerchoice):
    if playerchoice in ('rock') or playerchoice in ('paper') or playerchoice in ('scissors') or playerchoice in ('lizard'):
        return playerchoice[0] + computerchoice
    elif playerchoice in ('spock'):
        return 'k' + computerchoice
    else:
        print(f'You picked {playerchoice} which is not rock, paper or scissors. You fail for not following directions')
        quit()


def gamestate(gs):
    config = {
        'rr': {
            'out': 'We both played rock.',
            'winlosetie': 'draw'},
        'rp': {
            'out': 'My paper covers your rock.',
            'winlosetie': 'lose'},
        'rs': {
            'out': 'Your rock smashes my scissors',
            'winlosetie': 'win'},
        'rk': {
            'out': 'My spock vaporizes your rock',
            'winlosetie': 'lose'},
        'rl': {
            'out': 'Your rock crushes my lizard',
            'winlosetie': 'win'},
        'pr': {
            'out': 'Your paper covers my rock',
            'winlosetie': 'win'},
        'pp': {
            'out': 'We both played paper',
            'winlosetie': 'draw'},
        'ps': {
            'out': 'My scissors cut your paper',
            'winlosetie': 'lose'},
        'pk': {
            'out': 'Your paper disproves my spock',
            'winlosetie': 'win'},
        'pl': {
            'out': 'My lizard eats your paper',
            'winlosetie': 'lose'},
        'sr': {
            'out': 'My rock smashes your scissors',
            'winlosetie': 'lose'},
        'sp': {
            'out': 'Your scissors cut my paper',
            'winlosetie': 'win'},
        'ss': {
            'out': 'We both played scissors',
            'winlosetie': 'draw'},
        'sk': {
            'out': 'My spock smashes your scissors',
            'winlosetie': 'lose'},
        'sl': {
            'out': 'Your scissors decapitate my lizard',
            'winlosetie': 'win'},
        'kr': {
            'out': 'Your spock vaporizes my rock',
            'winlosetie': 'win'},
        'kp': {
            'out': 'My paper disproves your spock',
            'winlosetie': 'lose'},
        'ks': {
            'out': 'Your spock smashes my scissors',
            'winlosetie': 'win'},
        'kk': {
            'out': 'We both played spock',
            'winlosetie': 'draw'},
        'kl': {
            'out': 'My lizard poisons your spock',
            'winlosetie': 'lose'},
        'lr': {
            'out': 'My rock crushes your lizard',
            'winlosetie': 'lose'},
        'lp': {
            'out': 'Your lizard eats my paper',
            'winlosetie': 'win'},
        'ls': {
            'out': 'My scissors decapitate your lizard',
            'winlosetie': 'lose'},
        'lk': {
            'out': 'Your lizard poisons my spock',
            'winlosetie': 'win'},
        'll': {
            'out': 'We both played lizard',
            'winlosetie': 'draw'},
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
