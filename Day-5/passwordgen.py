import random
import string
from rich import print
from rich.console import Console


def main():
    length = get_length()
    password = generate_password(length)
    print(f"Your generated password is: [bold red]{password}[/bold red]")


def get_length():
    console = Console()
    length = int(console.input("How long would you like your password to be? "))
    return length


def get_alphas():
    console = Console()
    alphas = console.input("Do you want your password to include alpha characters? [bold green]True/False[/bold green] ").lower()
    if alphas in ("t", "true"):
        return True
    elif alphas in ("f", "false"):
        return False
    else:
        print(f"You typed {alphas} which is neither True nor False.  Try again.")
        get_alphas


def get_numbers():
    console = Console()
    numbers = console.input("Do you want your password to include numbers? [bold green]True/False[/bold green] ").lower()
    if numbers in ("t", "true"):
        return True
    elif numbers in ("f", "false"):
        return False
    else:
        print(f"You typed {numbers} which is neither True nor False.  Try again.")
        get_numbers()


def get_symbols():
    console = Console()
    symbols = console.input("Do you want your password to include symbols? [bold green]True/False[/bold green] ").lower()
    if symbols in ("t", "true"):
        return True
    elif symbols in ("f", "false"):
        return False
    else:
        print(f"You typed {symbols} which is neither True nor False.  Try again.")
        get_symbols()


def generate_password(length):
    choices=[]
    if get_alphas() == True:
        choices.append(string.ascii_letters)
    if get_numbers() == True:
        choices.append(string.digits)
    if get_symbols() == True:
        choices.append(string.punctuation)

    selections = []
    for row in choices:
        selections.extend(row)

    password = ""
    for c in range(length):
        password += random.choice(selections)

    return password


if __name__ == '__main__':
    main()
