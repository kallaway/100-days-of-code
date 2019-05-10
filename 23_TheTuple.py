#Day 23: Using the Tuple
#The following illustrates speeds on a highway during a random one-minute sample. First, the samples will be converted to kmph, then the resulting list will
#be turned into a tuple. Tuples are light on memory, giving them an advantage over lists. However, tuples are immutable, whereas lists are not. The immutable
#quality can be an advantage or disadvantage, so the use of a tuple must be carefully considered. 
#import array as arr														

def cmp(x, y):															#deprecated Python 2 standard library method
	return (x > y) - (x < y)

def mph_kmph_converter(speed_mph):										#mph to kmph is * 1.609 , interesting
	speed_kmph = speed_mph * 1.609
	return speed_kmph
	

																		#let's calculate kmph
highway_speeds_mph = [65, 71, 69, 49, 72, 69, 64, 74, 75, 68, 64, 64, 55, 73, 59, 72, 71, 73, 59, 51, 65, 69, 70, 79, 72, 71]
highway_speeds_kmph = []

for num in highway_speeds_mph:											#for loop calculates each value
	highway_speeds_kmph.append(mph_kmph_converter(num))

#print(highway_speeds_kmph)

mph_tuple = tuple(highway_speeds_mph)									#this makes the lists immutable - tuples!
kmph_tuple = tuple(highway_speeds_kmph)
print("  ")																#wrap function in str() for output
print("When comparing the two tuples, we get " + str(cmp(mph_tuple, kmph_tuple)))
print("  ")
print("Miles per hour readings, one minute: " + str(mph_tuple))
print("  ")
print("Kilometers per hour readings, one minute: " + str(kmph_tuple))

lengthmph = len(mph_tuple)												#these variables split the both the tuples in half
lengthkmph = len(kmph_tuple)
mphhalf = lengthmph//2 
kmphhalf = lengthkmph//2
mph_tuple_a = (mph_tuple[:mphhalf])
mph_tuple_b = (mph_tuple[mphhalf:])
print(mph_tuple_a)
print(mph_tuple_b)
kmph_tuple_a = (kmph_tuple[:kmphhalf])
kmph_tuple_b = (kmph_tuple[kmphhalf:])
print(kmph_tuple_a)
print(kmph_tuple_b)
