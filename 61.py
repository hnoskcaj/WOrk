# The best choise is to always switch. if you stay, you olbiously wil 1/3 of the time.
# however, if you switch you will win 2/3 of the time. if you choose either penny slot,
# the other one is revealed, so switching means getting the car, so two(choosing either
# penny door) choices gtes you a win when you switch


import random as r
Round = 0
ticker = 0
while Round < 10000:
	x = r.randint(1,3)
	if x == 3:
		ticker += 1
	Round += 1

# while Round < 10000:
# 	x = r.randint(1,3)
# 	if x == 1 or x== 2:
# 		ticker += 1
# 	Round += 1

print(ticker)


