#Day 6: The Monty Hall Problem
from random import seed													            #imports random modules
from random import randint
print('\n')																                  #draws the three doors
print('Please pick Door 1, 2, or 3 by typing the number below.')
print('\n')
print('\n')

print('         ________         ________         ________')
print('        |        |       |        |       |        |')
print('        |        |       |        |       |        |')
print('        |        |       |        |       |        |')
print('        |   1    |       |   2    |       |    3   |')
print('        |        |       |        |       |        |')
print('        |        |       |        |       |        |')
print('        |________|       |________|       |________|')
print('\n')

						  
first_choice = input()													          #Choose one door: 1, 2, or 3
first_choiceInt = int(first_choice)	
if (first_choiceInt==1) or (first_choiceInt==2) or (first_choiceInt==3):#set flag for correct input
	flag=0
	answerInt=first_choiceInt
else:																	                    #set flag for user error
	 flag=1

while flag==1:															              #keeps asking until they get it right
	
	answer = input("You have entered an invalid response. Please enter a 1, 2, or 3. ")
	answerInt = int(answer)
	if (answerInt == 1) or (answerInt == 2) or (answerInt ==3):
		
		
		flag=0
first_choiceInt = answerInt			
	
		


print("\nYou have picked Door number " + str(first_choiceInt) + ".")	
                                                          #Repeats door number
input()

actual = randint(1,3)													            #Door the Porsche will be under

MontyPick = randint(1,3)												          #Game show host picks this number
while (MontyPick == actual) or (MontyPick == first_choiceInt):
	MontyPick = randint(1,3)

input("\nYou may or may not have picked the right door. \n\nLet's see what is behind Door Number " + str(MontyPick) + ".")

input("\nBehind Door Number " + str(MontyPick) + ", we have a goat.")

new_answer = input("\nIf you would like to stay with the door you picked, type that number again.  If you would like to change doors, type that number.")
new_answerInt = int(new_answer)

if new_answerInt == actual:												        #Does the answer match the Porsche door?
	print("Congratulations! You win a new Porsche 911!")
else:
	print("You lose!")													            #Or do you get a slice of pepperoni pizza?

input()																	                  #User can press enter to exit
