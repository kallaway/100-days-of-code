# task 1
#if the first letter of the word is a costenant move that to the end and add "ay"
#if the first letter of the word is a vowel - just add "way" to the end.

#task 2
# function named numerus
#take roman numerals and output arabic numerals
# ie: xiv => 14
#mmxlix => 2049
#
#i = 1
#v = 5
#x = 10
#l = 50
#c = 100
#m = 1000
# unless a number below it is immedately preceding it
# eg iv = 4
# eg cm = 900

#Task 1
#We need to define a word
a_word = "working

#[0] will define our starting letter
a_word[0]
#W will be 0

a_word[1: ] + a_word[0]
#takes orking and adds the w

a_word[1: ] + a_word[0] + "ay"
#adds ay at the end

b_word = "oranges"
#word b has a vowel at the front

b_word + "way"
#adds way to the end


vowels = "aeiou"
#defining vowels

"a" in vowels
#test vowel

if a_word[0] in vowels:
    print(a_word + "way")
else:
    print(a_word[1: ] + a_word[0] + "ay")
#adding way to the end of a words


def igpay(a_word):
    vowels = "aeiouAEIOU"
    
    if a_word[0] in vowels:
        return (a_word + "way")
    else:
        return (a_word[1: ] + a_word[0] + "ay")
#creating the function




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
