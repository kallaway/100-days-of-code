#Day 14: Selection Sort
#Good information for the code logic found at interactivepython.org/lpomz "The Selection Sort"
#Selection sort simply passes through the list looking for values in order to place aside, putting them in order as it does so.
#The Selection Sort, as with the Bubble Sort, is light on memory. It is a bit faster to compute(but still considered slow), as it only has to go through less
#iterations. It is quicker to code than almost any other sorting algorithm. 
from time import sleep
import math
import copy 

numlist = [1,2,75,2,91,3,70,22,38,48]
length = len(numlist)
lengthInd = length - 1
print(numlist)
print("  ")                                                                 ##rangelist = len(number_list)
print("  ")                                                                 ##print(number_list)
                                                                            ##flag = True
                                                                            ##
                                                                            ##for i in range(0,100):
                                                                            ##    for x in number_list:
                                                                            ##        if flag == 0:
                                                                            ##            for y in range(0,9):
                                                                            ####            print(' ')
                                                                            ##                print(i)
                                                                            ##                print(x)
                                                                            ##                if x == i:
                                                                            ##                    pop = number_list.pop(y)
                                                                            ##                    number_list.append(pop)
                                                                            ##                    flag = False
                                                                            ##                if x == number_list[rangelist-1] and flag == False:
                                                                            ##                    flag = True
                                                                            ##                    i = i + 1
                                                                            ##                print(number_list)
                                                                            ####            print(' ')
            
            


for i in range(lengthInd, 0, -1):
    maxvalue = 0
    maxend = i + 1
    for a in range(1,maxend):
        if numlist[a] > numlist[maxvalue]:
            maxvalue = a
    
    arrtem = numlist[i]
    numlist[i] = numlist[maxvalue]
    numlist[maxvalue] = arrtem

print("  ")
print("SELECTION SORT")
print(numlist)
