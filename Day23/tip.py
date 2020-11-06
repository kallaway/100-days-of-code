print("Welcome to the tip calculator")

total = input("What was the total bill?\n")

how_many = input("How many people were in your group?\n")

tip_each = input("What tip do you want to leave? 12, 15, or 20 percent?\n")

tip = float(total) * (int(tip_each)/int(100))


per_person = float(tip / int(how_many))


print(f"The tip per person is {per_person} dollars")