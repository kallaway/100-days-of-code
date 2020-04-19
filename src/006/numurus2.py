#task 2

#numerus

def to_val(letter):
    if letter == "i" : return 1
    elif letter == "v" : return 5
    elif letter == "x" : return 10
    elif letter == "l" : return 50
    elif letter == "c" : return 100
    elif letter == "m" : return 1000
    return 0

total = 0; roman="mmcvi"

for l in roman:
     total += to_val(l)


#need to fix the xiv sol


def to_val(letter):
    if letter == "i" : return 1
    elif letter == "v" : return 5
    elif letter == "x" : return 10
    elif letter == "l" : return 50
    elif letter == "c" : return 100
    elif letter == "m" : return 1000
    return 0

total = 0; prev = 0; roman="xiv"

for l in roman:
    cur = to_val(l)
    if prev < cur:
        total -= prev
        cur -= prev
    total += cur
    prev = cur


#Final Product

def to_val(letter):
    if letter == "i" : return 1
    elif letter == "v" : return 5
    elif letter == "x" : return 10
    elif letter == "l" : return 50
    elif letter == "c" : return 100
    elif letter == "m" : return 1000
    return 0
    
def numurus(roman):
    total = 0
    prev = 0
    for l in roman:
        cur = to_val(l)
        if prev < cur :
            total -= prev
            cur -= prev
        total += cur
        prev = cur
    return total