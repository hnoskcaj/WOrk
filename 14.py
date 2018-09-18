import random as r
x = r.randrange(0,10,1)

def guess():
	if x == int(input("Guess agian 1-10! ")):
		print("You got it!")
		exit()
	else:
		guess()

 
if x == int(input("Guess which number im thinking of 1-10! ")):
	print("You got it!")
else:
	guess()





