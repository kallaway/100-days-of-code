#None - null


# >>> my_data= ""
# >>> if my_data: print("Got data?")
# ...
# >>> my_data
# ''
# >>>
# >>> my_data = None
# >>> if my_data: print("Got data?")
# ...
# >>>
# >>>
# >>>
# >>>
# >>> my_data= "Yes"
# >>> if my_data: print("Got data?")
# ...
# Got data?
# >>>
# KeyboardInterrupt
# >>>


None 


my_data = " "


if my_data is None"
    print("Not set!")

my_data = 0

my_data = None

if my_data is None:
    print("Not set!")

my_data = None

if my_data is not None:
    print("Anything!")

    >>> if my_data is not None:
...     print("Anything!")



#Dictionaries can store more than one piece of data at a time.
#Lists and Dictionaries
#Dictionaries are unordered
#If a string is different in any way - it is a different string.

cats = {}
a_list = []

cats["Robin"] = 5
cats["Adrian"] = 2
cats["Camilla"] = 1

#get command can also get values

cats.get("Bobbie")

cats.get("Adrian")

# >>> cats.get("Bobbie")
# >>> cats.get("Adrian")
# 2
# >>>
# >>> print(cats.get("Bobbie"))
# None
# >>>

cats.get("Bobbie", 0)
#Returns 0


"Robin" in cats
# >>> "Robin" in cats
# True

2 in cats

# >>> 2 in cats
# False
# >>>

>>> cats
{'Robin': 5, 'Adrian': 2, 'Camilla': 1}
>>> for name in cats:
...     print(name)
...
Robin
Adrian
Camilla
>>>

for name in cats:
    print("{0} has {1} cat(s)" .format(name, cats [name]))

#or

for name in cats.keys():
    print("{0} has {1} cat(s)" .format(name, cats [name]))

#If we only want the vaulues
for num_cats in cats.values():
    print(num_cats)

for (person, num_cats) in cats.items():
    print(person)
    print(num_cats)

#removing

del cats["Robin"]

cats.pop("Robin")

#Example of LIST from Drop down HTML page

countries = { "AF": "Afganistan", "AL": "Albania", "DZ": "Algeria"}

for (code, country) in countries.items():
    print('<option value="{0}">{1}</option>'.format(code, country))

#Performance is a reason to take a dictionary over a list


thumbnail = None
cond = "Cloudy"

if cond == "Rainy": thumbnail = "rain.png"


weather = {"Rainy": "rain.png", "Cloudy": "clouds.png"}


weather [cond]
'clouds.png'

thumbnail = weather.get(cond)

users = {1: {"name": "Joe", "email": "joe@example.com"}, 2: {"name": "Sarah", "email": "sarah@example.com"}}
