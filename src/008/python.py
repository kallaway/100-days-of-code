#This portion will load the dictionary and the values to the related numeral letters

def to_val(letters):
    letters["i"] = 1
    letters["v"] = 5
    letters["x"] = 10
    letters["l"] = 50
    letters["c"] = 100
    letters["m"] = 1000
    print(letters.__str__)
    return 0

#This will set total to 0 and then whatever the numerals we want in roman pulls values from correlated number
total = 0; roman="mmcvi"

#Assigns total to l and =+ tp total from numeral
for l in roman:
     total += to_val(l)

#currently fails