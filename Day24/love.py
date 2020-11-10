# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1 + name2

tCount = names.count("t")
rCount = names.count("r")
uCount = names.count("u")
eCount = names.count("e")
lCount = names.count("l")
oCount = names.count("o")
vCount = names.count("v")
leCount = names.count("e")

trueCount = tCount + rCount + uCount + eCount
print(trueCount)
loveCount = lCount + oCount + vCount + leCount
print(loveCount)
total = int(str(trueCount) + str(loveCount))

if total < 10 or total > 90:
    print(f"Your score is {total}. You go together like coke and mentos")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")







