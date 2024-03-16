'''
# Example usage
What was the total bill? $124.54
How many people to split the bill? 5
What percentage tip would you like to give? 10, 12, or 15? 12
Each person should pay: $27.9
'''


def main():
    print('Welcome to the tip calculator.')
    totalbill = input('What is the total bill? ')
    payers = input('How many people will split the bill? ')
    tippercent = input('What percentage tip would you like to give? 10, 15, or 20? ')

    bill = processbill(totalbill)
    tip = validatedip(tippercent)
    pay = calculateresult(bill, tip, int(payers))

    print('Each person should pay ${:.2f}'.format(pay))


def processbill(totalbill):
    if totalbill[0] == '$':
        return float(totalbill[1:])
    return float(totalbill)


def validatedip(tippercent):
    if type(tippercent) is str:
        tippercent = int(tippercent)

    if is_member(tippercent, [10, 15, 20]):
        return tippercent
    print('You must select one of the following tip values: 10, 15, or 20')
    quit()


def calculateresult(bill, tip, payers):
    cost = ((bill * tip) / 100) + bill
    costperperson = cost/payers
    return costperperson


def is_member(value, iterable):
    for item in iterable:
        if value is item or value == item:
            return True
    return False


if __name__ == '__main__':
    main()
