9/10 chat-bot anh.cs.luc.edu

print("Hi! what's your name")
username = input('your name_')
print ("Hello__" + username)
answer1 = input ('Spell Hop_')
if answer1 == "hop" or answer1 == "Hop":
	print ("yes")
	answer2 = input ('Spell Top_')
	if answer2 == "top" or answer2 == "Top":
		print ("yes")
		answer3 = input ('spell Mop_')
		if answer3 == "mop" or answer3 == "Mop":
			print ("yes")
			answer4 = input ('what do you do at a green light?')
			if answer4 == "go" or answer4 == "Go":
				print ("Congrats!")
			else: print("No silly you GOOOO!")
		else: print ("No")
	else: print ("No")
else: print ("No")