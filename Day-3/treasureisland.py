import subprocess, os


def main():
    clearscreen()
    welcome()
    crossroads()
    lake()
    house()
    win()


def crossroads():
    direction = input('You are at cross road.  Where do you want to go?  Type "left" or "right" ')
    if direction.lower() in ("r", "right"):
        print('You fell into a hole.  Game Over.')
        quit()
    else:
        return True


def lake():
    cross = input('You have come to a lake.  There is an island in the middle of the lake.  Type "wait" to wait for a boat.  Type "swim" to swim across.')
    if cross.lower() in ('s', 'swim'):
        print('You get attacked by an angry trout.  Game Over.')
        quit()
    else:
        return True


def house():
    door = input("You arrive at the island unharmed.  There is a house with 3 doors.  One red, one yellow, and one blue.  Which color do you choose?")
    if door.lower() in ('r', 'red'):
        print('It is a room full of fire. Game Over.')
        quit()
    elif door.lower() in ('b', 'blue'):
        print('You enter a room full of beasts.  Game Over')
        quit()
    elif door.lower() in ('y', 'yellow'):
        print('You have found the treasure.  You Win!')
        return True
    else:
        print('You are not very good at following directions.  You are eaten by a gru.  Game Over!')
        quit()


def win():
    print('''
    ******************************************************************************* 
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')


def welcome():
    print('Welcome to Treasure Island.')
    print('Your mission is to find the treasure.')
    return


def clearscreen():
    if os.name is 'posix':
        os.system('clear')
        return True
    elif os.name is 'nt':
        os.system('cls')
        return True
    else:
        return True


if __name__ == '__main__':
    main()
