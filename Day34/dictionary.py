programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    
}

#retrieving items from a dictionary
print(programming_dictionary["Bug"])

# to add a new entry
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#Create an empty dictionary
# empty_dictionary = {}

# wipe and existing dictionary
# programming_dictionary = {}

# Edit an item
programming_dictionary["Bug"] = "This is edited text."
print(programming_dictionary)

#Loop - only prints key!
for item in programming_dictionary:
    print(item)

# Use this instead
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])