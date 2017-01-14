#!/usr/bin/env python

with open("animals.txt","r") as file:

	i = 0

	occurence = {}

	for line in file:

		
		key = line.rstrip('\n')

		if key in occurence:
			occurence[key] += 1
		else:
			occurence[key] = 1

	print occurence