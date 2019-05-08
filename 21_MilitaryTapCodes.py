#Day 21: Tap Code
#During the U.S./Vietnam War, US POWs used a system of tap codes to communicate with one another. Important messages between troops in different cells could
#be communicated quietly using this system. 


import winsound																					#imports sound in same folder as application
from time import sleep																			#sleep timer is used for spacing between taps

print("")
print("")
print("")
print("")
print("")
print("                                 _______________________________________________")
print("                                | TAP   |       |       |       |       |       |")                                                 
print("                                | CODE  |   1   |   2   |   3   |   4   |   5   |")
print("                                |       |       |       |       |       |       |")
print("                                |_______|_______|_______|_______|_______|_______|")
print("                                |       |       |       |       |       |       |")
print("                                |   1   |   A   |   B   |  C/K  |   D   |   E   |")
print("                                |       |       |       |       |       |       |")
print("                                |_______|_______|_______|_______|_______|_______|")
print("                                |       |       |       |       |       |       |")
print("                                |   2   |   F   |   G   |   H   |   I   |   J   |")
print("                                |       |       |       |       |       |       |")
print("                                |_______|_______|_______|_______|_______|_______|")
print("                                |       |       |       |       |       |       |")
print("                                |   3   |   L   |   M   |   N   |   O   |   P   |")
print("                                |       |       |       |       |       |       |")
print("                                |_______|_______|_______|_______|_______|_______|")
print("                                |       |       |       |       |       |       |")
print("                                |   4   |   Q   |   R   |   S   |   T   |   U   |")
print("                                |       |       |       |       |       |       |")
print("                                |_______|_______|_______|_______|_______|_______|")
print("                                |       |       |       |       |       |       |")
print("                                |   5   |   V   |   W   |   X   |   Y   |   Z   |")
print("                                |       |       |       |       |       |       |")
print("                                |_______|_______|_______|_______|_______|_______|")
print("")
print("")
print("")
print("")
input()																							#press enter

def tapper():																					#pulls tap sound from folder and plays it (.wav)
	winsound.PlaySound("tap", winsound.SND_ASYNC)

def tap_code(array):																			#main function assigns a tap combo to each letter
	for i in array:
		if i == 'A':
			for i in range(1,2):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,2):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'B':
			for i in range(1,3):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,2):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'C' or i == 'K':
			for i in range(1,4):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,2):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'D':
			for i in range(1,5):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,2):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'E':
			for i in range(1,6):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,2):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'F':
			for i in range(1,2):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,3):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'G':
			for i in range(1,3):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,3):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'H':
			for i in range(1,4):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,3):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'I':
			for i in range(1,5):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,3):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'J':
			for i in range(1,6):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,3):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'L':
			for i in range(1,2):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,4):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'M':
			for i in range(1,3):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,4):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'N':
			for i in range(1,4):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,4):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'O':
			for i in range(1,5):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,4):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'P':
			for i in range(1,6):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,4):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'Q':
			for i in range(1,2):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,5):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'R':
			for i in range(1,3):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,5):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'S':
			for i in range(1,4):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,5):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'T':
			for i in range(1,5):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,5):
				sleep(.30)
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'U':
			for i in range(1,6):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,5):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'V':
			for i in range(1,2):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,6):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'W':
			for i in range(1,3):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,6):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'X':
			for i in range(1,4):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,6):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'Y':
			for i in range(1,5):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,6):
				
				tapper()
				sleep(.20)
			sleep(1)
		if i == 'Z':
			for i in range(1,6):
				tapper()
				sleep(.20)
			sleep(.30)
			for i in range(1,6):
				
				tapper()
				sleep(.20)
			sleep(1)	
word = input("Spell your word and press enter.")												#asks for user input

#print(word)

array1 = list(word)


length_index = len(array1)-1


tap_code(array1)



input()
