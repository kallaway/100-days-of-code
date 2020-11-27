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

num1 = int(input("What is the first number?\n"))
symbol_operator = input("Pick an operation from the lines above: ")
num2 = int(input("What is the second number?\n "))

for symbol in calculator_functions:
    print(symbol)



calculate = calculator_functions[symbol_operator]
answer = calculate(num1, num2)

print(f"{num1} {symbol_operator} {num2} = {answer}")