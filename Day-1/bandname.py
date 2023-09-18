import requests


def main():
    print('Do you want to use a random band name? Yes/No')
    selection = input()
    if selection in ('y', 'yes'):
        bandname = []
        for w in range(2):
            word = getword()
            bandname.append(word)
        print(f'Your band name should be {bandname[0]} {bandname[1]}')
    else:
        bandname = coursename()
        print(f'Your band name should be {bandname}')


def getword():
    return requests.get('https://random-word-api.herokuapp.com/word').json()[0]


def coursename():
    city = input('What city did you grow up in? ')
    pet = input('What was the name of your favorite pet? ')
    return f'{city} {pet}'


if __name__ == '__main__':
    main()
