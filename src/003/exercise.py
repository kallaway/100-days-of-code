# This is a blank document that will be built into a deck of cards.
# Starting with 1 and double the number until it is at least 1 Trillion.

deck = [ "Ace of Spades", "Aces of Hearts", "Ace of Clubs", "Ace of Diamonds", 
"Two of Spades", "Two of Hearts", "Two of Clubs", "Two of Diamonds",
"Three of Spades", "Three of Hearts", "Three of Clubs", "Three of Diamonds",  
"Four of Spades", "Four of Hearts", "Four of Clubs", "Four of Diamonds",
"Five of Spades", "Five of Hearts", "Five of Clubs", "Five of Diamonds",
"Six of Spades", "Six of Hearts", "Six of Clubs", "Six of Diamonds",
"Seven of Spades", "Seven of Hearts", "Seven of Clubs", "Seven of Diamonds",
"Eight of Spades", "Eight of Hearts", "Eight of Clubs", "Eight of Diamonds",
"Nine of Spades", "Nine of Hearts", "Nine of Clubs", "Nine of Diamonds",
"Ten of Spades", "Ten of Hearts", "Ten of Clubs", "Ten of Diamonds",
"Jack of Spades", "Jack of Hearts", "Jack of Clubs", "Jack of Diamonds",
"Queen of Spades", "Queen of Hearts", "Queen of Clubs", "Queen of Diamonds",
"King of Spades", "King of Hearts", "King of Clubs", "King of Diamonds",
]





number = 1

while number <= 1000000000000:
    print(str(number))
    number *=2



print("Hello")

len("Sausage")

abs(1235)

bin(123)

round(3.14)

sum([1,2,3,4])

max([-50, 100, 1000])

min([-50, 100, 1000])

for x in range(10): print(x)




sorted("abracadabra")

reversed(sorted("abracadabra"))

list(reversed(sorted("abracadabra"))

''.join(reversed(sorted("abracadabra")))

''.join(reversed(sorted(["Alice", "Bob", "Mike"])))

'This is a long string'.split(" ")
['This', 'is', 'a', 'long', 'string']

"There are " + str(5) + " items in your cart"

a_list ['This', 'a', 'is', 'long', 'string']
a_list.reverse()

a_list.pop()

a_list.remove('long')

b_list = a_list

c_list = a_list.copy()

c_list.append("Owls")


def noop(): pass
#does nothing

def greet(name): print ("Hello, {0}".format(name))

greet("Robin")


def product(numbers):
    p = 1
    for n in numbers:
        p *= n
    return p

product([1, 2, 3, 4])

def combine_and_sort(first, second):
    return sorted((first + second))

combine_and_sort([1, 3, 5], [2, 4, 6])


def naughty_product(numbers):
    p = 1
    while numbers:
        p *= numbers.pop()
    return p

    naughty_product([1, 2, 3, 4])




