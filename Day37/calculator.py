from art import logo

print(logo)
# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2


# Create a dictionary
calculator_functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():

    num1 = float(input("What is the first number?\n"))
    for symbol in calculator_functions:
        print(symbol)
    should_continue = True

    while should_continue: 
        symbol_operator = input("Pick an operation from the lines above: ")
        num2 = float(input("What is the next number?\n"))
        calculate = calculator_functions[symbol_operator]
        answer = calculate(num1, num2)

        print(f"{num1} {symbol_operator} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' start a new calculation.\n") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()