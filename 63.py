# the longest walk you can take with a greater that 50% chance of walking hom eis 22
# blocks, though there are shorter walks that will have a lower chance of walking home.

# Monte Carlo simulation-
# using randomely genreated inputs to create a wide rang eof outputs to better predict future
# outcomes using lont of randome samples. they can be uses to predict stock matkets of other
# variables based on previous data, and to determine the most likely ourcome as well as other
# possabilities.

# Darts-
# the values gets closer to π. and start to take a long a** time to compute


#----------------RANDOM WALK---------------------

import random as r
import math as m
def randwalk(n):
	x = 0
	xx = 0
	y = 0
	yy = 0
	count = 0
	walk = 0
	global a
	while count < n:
		num = r.randint(1,4)
		#choose a random number, where each number corresponds to a direction
		if num == 1:
			xx +=1
			#1 = right
		if num == 2:
			xx -=1
			#2 = left
		if num == 3:
			yy +=1
			#3 = up
		if num == 4:
			yy -=1
			#4 = down
		count += 1
		#takes the absolute value of the total x and y components, and adds them together to get
		#the total distance.
	walk = (m.sqrt(xx**2)+m.sqrt(yy**2))
	#if the distance is greater than 4 as a ticker to a
	if walk > 4:
		a += 1
global a
a = 0
b = 0
while b <1000:
	randwalk(15)
	b+= 1
print(a)



#----------DARTBOARD CODE-------------

import random as r
a = 0
#NUMBER OF ITERATIONS
z = 100000000
count = 0
while count < z:
	#random spon in the area
	x = r.uniform(0,4)
	# there is 3.14 swuare inches of space in the circle and t0.86 remaining in the square
	#this is simulated bu the numbers
	if x <= 3.14:
		a += 1
	count += 1
print(a)
print(a*4/z)