import random

matrix = [[0.64, 0.32, 0.04], 
		 [0.4, 0.5, 0.1], 
		 [0.25, 0.5, 0.25]]

state = random.choice([0, 1, 2])
counts = [0,0,0]

for i in xrange( 10000 ):
	counts[state] += 1
	rand = random.random()

	if rand <= matrix[state][0]:
		state = 0
	elif rand <= matrix[state][0] + matrix[state][1]:
		state = 1
	else:
		state = 2

for i in range( len( counts ) ):
	print( "State " + str(i) + ": " + str(counts[i] ) )

