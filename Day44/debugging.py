############DEBUGGING#####################

# Describe Problem
# for loop is looping through 1 through 20. When I equals 20, the print statement should execute.
# But the loop has to run all the way to the end. Why not just use the if statement alone?
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # was (1,6) originally
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# Fix the Errors
 # was age = input("How old are you? ")
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.")

#Print is Your Friend
# ******************* ORIGINAL CODE *********************************
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# ******************* fixed  CODE *********************************
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages)
# word_per_page = int(input("Number of words per page: "))
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)
# ******************************************************************
# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])