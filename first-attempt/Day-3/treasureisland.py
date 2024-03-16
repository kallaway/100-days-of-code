import subprocess, os
from drawing import asciiart
import time


def main():
    clearscreen()
    welcome()
    crossroads()
    lake()
    house()
    win()


def crossroads():
    gs = 0
    asciiart(gs)
    direction = input('You are at cross road.  Where do you want to go?  Type "left" or "right" ')
    if direction.lower() in ("r", "right"):
        gs = 3
        asciiart(gs)
        print('You fell into a hole.  Game Over.')
        quit()
    else:
        time.sleep(3)
        clearscreen()
        return True


def lake():
    gs = 1
    asciiart(gs)
    cross = input('You have come to a lake.  There is an island in the middle of the lake.  Type "wait" to wait for a boat.  Type "swim" to swim across. ')
    if cross.lower() in ('s', 'swim'):
        gs = 4
        asciiart(gs)
        print('You get attacked by an angry trout.  Game Over.')
        quit()
    else:
        time.sleep(3)
        clearscreen()
        return True


def house():
    gs = 2
    asciiart(gs)
    door = input('You arrive at the island unharmed.  There is a house with 3 doors.  One red, one yellow, and one blue.  Which color do you choose? ')
    if door.lower() in ('r', 'red'):
        clearscreen()
        gs = 5
        asciiart(gs)
        print('It is a room full of fire. Game Over.')
        quit()
    elif door.lower() in ('b', 'blue'):
        gs = 6
        clearscreen()
        asciiart(gs)
        print('You enter a room full of beasts.  Game Over')
        quit()
    elif door.lower() in ('y', 'yellow'):
        clearscreen()
        print('You have found the treasure.  You Win!')
        return True
    else:
        print('You are not very good at following directions.  You are eaten by a gru.  Game Over!')
        quit()


def win():
    gs = 7
    asciiart(gs)


def welcome():
    print('Welcome to Treasure Island.')
    print('Your mission is to find the treasure.')
    time.sleep(3)
    return


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
