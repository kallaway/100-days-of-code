#Notes
#Binary data cannot be stored in Dicts / Lists / etc
#Tuple vs Lists

fruits = ("Apple", "Orange", "Lemon", "Tomato")
for f in fruits: print("Would you like a nice " + f + "?")

# >>> fruits.append("Strawberry")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'append'

red = (255, 0, 0 )

purple = (255, 0, 255)

grades = ( [95, 90], [50, 90])
grades [1]
grades [1][0] = 100

# >>> grades = ( [95, 90], [50, 90])
# >>> grades [1]
# [50, 90]
# >>> grades [1][0] = 100
# >>>
# >>> grades
# ([95, 90], [100, 90])
# >>>

#set

[list]
(tuple)
{sets}

vegetables = {"Carrot", "Onion", "Tomato"}

#sets can be popped
vegetables.pop()

# >>> vegetables.pop()
# 'Carrot'
# >>> for v in vegetables: print(v)
# ...
# Tomato
# Onion
# >>>

vegetables.add("Radish")


vegetables.intersection(fruits)
{'Tomato'}


>>> for v in vegetables: print(v)
...
Radish
Tomato
Onion
>>> vegetables.intersection(fruits)
{'Tomato'}
>>> {'Tomato'}
{'Tomato'}
>>> fruits
('Apple', 'Orange', 'Lemon', 'Tomato')
>>> vegetables
{'Radish', 'Tomato', 'Onion'}
>>> set(fruits)
{'Orange', 'Apple', 'Tomato', 'Lemon'}
>>> list(set(tuple(vegetables)))
['Radish', 'Tomato', 'Onion']
>>>


frozen = frozenset(vegetables)

frozen.pop()
#will not work


for l in "A string": print(l)

>>> for l in "A string": print(l)
...
A

s
t
r
i
n
g
>>>

for i in ["a", "list", "of", "Strings"]: print(i)
>>> for i in ["a", "list", "of", "Strings"]: print(i)
...
a
list
of
Strings
>>>

for k in { "this": 4, "is": 2, "a": 1, "dict": 4 }: print(k)
>>> for k in { "this": 4, "is": 2, "a": 1, "dict": 4 }: print(k)
...
this
is
a
dict
>>>
colors = {"Red": (255, 0, 0), "Yellow": (255, 255, 0), "Purple": (255, 0, 255)}
for (name, rgb) in colors.items(): print(name, rgb)
...
Red (255, 0, 0)
Yellow (255, 255, 0)
Purple (255, 0, 255)
>>>

fruits

for (i, c) in enumerate(fruits): print(i,c)
>>> for (i, c) in enumerate(fruits): print(i,c)
...
0 Apple
1 Orange
2 Lemon
3 Tomato
>>>

for (f, v) in zip(fruits, vegetables): print(f, v)
>>> for (f, v) in zip(fruits, vegetables): print(f, v)
...
Apple Radish
Orange Tomato
Lemon Onion
>>> fruits
('Apple', 'Orange', 'Lemon', 'Tomato')
>>> vegetables
{'Radish', 'Tomato', 'Onion'}
>>> vegetables.add("Rhubarb")
>>> for (f, v) in zip(fruits, vegetables): print(f, v)
...
Apple Radish
Orange Rhubarb
Lemon Tomato
Tomato Onion
>>>


haystack = [ "hey" ] * 20
haystack[6] = "needle"

idx = None
for (i, v) in enumerate(haystack):
    print("Looking...")
    if v == "needle":
        idx = i
        print("FOUND IT!!!")


>>> for (i, v) in enumerate(haystack):
...     print("Looking...")
...     if v == "needle":
...         idx = i
...         print("FOUND IT!!!")
...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
FOUND IT!!!
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
>>>

haystack[idx]


idx = None
for (i, v) in enumerate(haystack):
    print("Looking...")
    if v == "needle":
        idx = i
        print("FOUND IT!!!")
        break

    >>> idx = None
>>> for (i, v) in enumerate(haystack):
...     print("Looking...")
...     if v == "needle":
...         idx = i
...         print("FOUND IT!!!")
...         break
...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
FOUND IT!!!
>>>

for (i, v) in enumerate(haystack):
    print("Looking...")
    if v == "hey":
            continue 
    idx = i
    print("FOUND IT!!!")
    break


>>> for (i, v) in enumerate(haystack):
...     print("Looking...")
...     if v == "hey":
...             continue
...     idx = i
...     print("FOUND IT!!!")
...     break
...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
FOUND IT!!!
>>>

haystack = [ "hey"] * 20

for (i, v) in enumerate(haystack):
    print("Looking...")
    if v == "hey":
            continue 
    idx = i
    print("FOUND IT!!!")
    break
else:
    print("Couldnt find it...:(")

    >>> for (i, v) in enumerate(haystack):
...     print("Looking...")
...     if v == "hey":
...             continue
...     idx = i
...     print("FOUND IT!!!")
...     break
... else:
...     print("Couldnt find it...:(")
...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Looking...
Couldnt find it...:(
>>>





