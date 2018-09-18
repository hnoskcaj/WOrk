#YOu guess an number, and it will remember,
#and print out the ones you've guessed before is askes again

#sources:programiz.com and docs.python.org

import random as r
x = r.randrange(0,10,1)

def guess():
	global List
	print("You've already guessed " + str(List))
	z = int(input("Guess agian 1-10! "))
	if x == z:
		print("You got it!")
		exit()
	else:
		List = List + ", " + str(z)
		guess()

z = int(input("Guess which number im thinking of 1-10! ")) 
if x == z:
	print("You got it!")
else:
	List = str(z)
	guess()





