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
    vowels = "aeiou"
    
    if a_word[0] in vowels:
        print(a_word + "way")
    else:
        print(a_word[1: ] + a_word[0] + "ay")
#creating the function