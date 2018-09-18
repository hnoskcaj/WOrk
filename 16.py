import time as t
slow = 0
bag = 0
lives = 3
def wakeup():
	
	print("You wake up in the pitch black dark. You have no idea where you are, or how you got there. The ground is hard, cold and slightly damp.")
	a = input("You are exausted out of your mind, are you going to \n(A) get up and feel aroung in the dark \n(B) go back to sleep?\n> ")
	if a == "a" or a == "A":
		t.sleep(slow)
		lookaround()
	elif a == "b" or a == "B":
		t.sleep(slow)
		sleep()
	else:
		print("\nplease enter 'a' or 'b'\n\n\n")
		t.sleep(slow)
		t.sleep(3)
		wakeup()

def sleep():
	global slow
	print("Congrats, while you were sleeping you fell into a state of hypothermia, not all of your movements and decisions will take an extra 2 seconds.\n\n\n")
	slow = slow + 2
	t.sleep(3)
	wakeup()

def lookaround():
		print("You start to feel your way around, noting that the floor is a cold stone, littered with puddles of slimmey water. You feel something furry brush your leg. Are you going to")
		a = input("(A) try to pick it up\n(B) scramble away")
		if a == "a" or a =="A":
			pickup()
		elif a =="b" or a =="B":
			scramble()
		else:
			print("\nplease enter 'a' or 'b'\n\n\n")
			t.sleep(3)
			lookaround()

def pickup():
	global slow
	t.sleep(slow)
	print("Great job! you've discovered a jacket! This will take away any hypothermia you already have, speeding up your gameplay.")
	slow = 0
	move1()
def scramble():
	global bag
	global slow
	t.sleep(slow)
	print("As you flee the mystery object, you put yous hand down on a course fabric. Quickly you realize that it's a bag. Will it be usefull?")
	a = input("(A) Pick is up! Ill use it.\n(B) I don't want it to slow me down.")
	if a == "a" or a == "A":
		bag = 1
		move1()
	if a =="b" or a == "B":
		bag = 0
		move1()
	else:
		print("\nplease enter 'a' or 'b'\n\n\n")
		t.sleep(3)
		scramble()

def move1():
	global slow
	print("You feel your way along a wall, as you walk, you feel what seels like a lever on the wall\n")
	a = input("(A Pull it! Twist it! Bop it!\n(B) Hell nah, I'm not touching that!")
	if a == "a" or a == "A":
		print("Why would you pull a rondom lever in a dark hallway????? You're dumb so it opened a trap door into a shollow stream you fell and broke your legs. Now you're slowed by 2 seconds and lost half a life. You can also now only cary two items in your bag.")
		slow = slow + 2
		t.sleep(slow)
		stream()
	if a =="b" or a == "B":
		print("A good choice, or a missed oportunity? youll never know.")
		move2()
	else:
		print("\nplease enter 'a' or 'b'\n\n\n")
		t.sleep(3)
		move1()


	

wakeup()