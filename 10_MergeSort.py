#Day 10: Merge Sort
#Ideas from Coding Blocks Youtube Channel Episode 84: Algorithms You Should Know
#https://www.youtube.com/watch?v=5R80MfMxtx4&list=PLWWyzc5ehM92EyZYAL5e5i2zfVqeXY0DA&index=13&t=0s
#Thank you also to Interactive Python website:
#http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html

#--------------------------------------------------------------------------------------------------------------------+
#2 Merge Sort: "Divide and Conquer"-this method splits the list in half, and continues to split each half until
#  there consists all pairs. At that point, the pairs are resorted back up to form a sorted list. 
#  very common algorithm  
#  time to code=slow; time to run=fast; memory required=high


from time import sleep

list1 = [16,10,6,17,4,1,1,20,2,18]

print("Your current list is " + str(list1))

def merger(list1):                                              #defines method to perform Merge Sort
    if len(list1)>1:
        
        mid = len(list1)//2                                     #splits n in half to begin algorithm
        sideleft = list1[:mid]                                  #left side
        sideright = list1[mid:]                                 #in an odd sample, the right side will include one more than left
        merger(sideleft)                                        #runs the method on each side
        merger(sideright)

        a=0
        b=0
        c=0
        while a < len(sideleft) and b < len(sideright):         #iterating through the sides,
            if sideleft[a] < sideright[b]:                      #breaking them in half each time
                list1[c]=sideleft[a]
                a=a+1
            else:
                list1[c]=sideright[b]
                b=b+1
            c=c+1

        while a < len(sideleft):
            list1[c]=sideleft[a]
            a=a+1
            c=c+1

        while b < len(sideright):
            list1[c]=sideright[b]
            b=b+1
            c=c+1
sleep(5)                                                        #sleeps for two seconds
merger(list1)                                                   #calls our method
print(" ")
print("MERGE SORT")
print("Your sorted list is "  + str(list1))                     #prints new list, sorted from least to greatest
