MENU = {
    "espresso": {
        "ingredients": {
            "water": 1,
            "coffee": 1,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 1,
            "milk": 9,
            "coffee": 2,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 1,
            "milk": 3,
            "coffee": 2,
        },
        "cost": 3.00,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: #1. Check if we have enough supplies to make the drinks


def is_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item} for you order. Please try something else.")
            return False
    return True

# TODO #2. Ensure enough money is entered for drink order


def count_coins():
    total = int(input("How many quarters did you put in my coin slot? ")) * 0.25
    total += int(input("How many dimes did you put in my coin slot? ")) * 0.10
    total += int(input("How many nickels did you put in my coin slot? ")) * 0.05
    total += int(input("How many pennies did you put in my coin slot? ")) * 0.01
    return total


def successful_transaction(coins_received, drink_price):
    if coins_received >= drink_price:
        change = round(coins_received - drink_price, 2)
        print(f"You gave me ${coins_received}. The total cost is ${drink_price}. Your change is ${change}")
        global profit
        profit += drink_price
        return True
    else:
        print(f"Sorry, that is not enough money. I have refunded you the ${coins_received}.")
        return False


def make_order(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Be careful it's hot!")


is_on = True


while is_on:
    choice = input("What would you like? (Espresso, Latte, or Cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}fl oz.")
        print(f"Milk: {resources['milk']}fl oz.")
        print(f"Coffee: {resources['coffee']} oz.")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_enough(drink["ingredients"]):
            payment = count_coins()
            if successful_transaction(payment, drink["cost"]):
                make_order(choice, drink["ingredients"])



