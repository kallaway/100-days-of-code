# Review: 
# Create a function called greet(). 
# def greet():
# # Write 3 print statements inside the function.
#   print("Hello")
#   print("Another print statment")
#   print("yet another print")
# # Call the greet() function and run your code.
# greet()

# def greet_with_name(name):
#   print(f"Hello, {name}")
#   print(f"Another print statment {name}")
#   print(f"Hey {name}. yet another print")

# greet_with_name("Bill")

#functions with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is the weather in {location}?")
    

greet_with("Bill", "Tucson")

#Functions with keyword arguments
greet_with(name="Bill", location="Somewhere")