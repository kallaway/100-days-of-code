#!/usr/bin/python3
from random import choice

draft_order = []
teams = ['FreshTaco', 'ANGRY_BIRDS!', '@RotoHack', '@GoutDracula', '@mhoerchler', '@djforbes7', '@Southpawd1213', '@briansoik', '@circulargenius']

balls = 9
lotto_balls = []
for team in teams:
	lotto_balls = lotto_balls + [team] * balls
	balls = balls - 1

print("Num lotto balls")
for team in teams:
	count = lotto_balls.count(team)
	print(team + " - " + str(count))

print("Draft Order")
for i in range(0,9):
	# randomly select a ball
	draft_order.append(choice(lotto_balls))
	num_balls = lotto_balls.count(draft_order[i])

	# need to remove all balls for person selected
	for j in range(num_balls):
		lotto_balls.remove(draft_order[i])
	
	# print the draft order
	print(repr(i+1) + '.) ' + repr(draft_order[i]))
