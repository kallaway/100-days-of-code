print("Welcome to the tip calculator")

total = float(input("What was the total bill?\n$"))

tip_each = int(input("What percentage tip would you like to leave? 12, 15, or 20?\n"))

how_many = int(input("How many people were in your group?\n"))

tip = total * (tip_each / 100) + total


per_person = round(tip / how_many,2)


print(f"The tip per person is: ${per_person} dollars each")