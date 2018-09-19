import time as t
slow = 0
bag = 0
clothing = 0
lives = 3
key = "stream"
def start():
	global slow
	global bag
	global clothing
	global lives
	global key
	print("You now have " + str(lives) + " lives")
	t.sleep(slow)
def wakeup():
	start()
	print("You wake up in the pitch black dark. You have no idea where you are, or how you got there. The ground is hard, cold and slightly damp.")
	a = input("You are exausted out of your mind, are you going to \n(A) get up and feel aroung in the dark \n(B) go back to sleep?\n> \n")
	if a == "a" or a == "A":
		lookaround()
	elif a == "b" or a == "B":
		sleep()
	else:
		print("\nplease enter 'a' or 'b'\n\n\n")
		t.sleep(3)
		wakeup()

def sleep():
	start()
	print("Congrats, while you were sleeping you fell into a state of hypothermia, not all of your movements and decisions will take an extra 2 seconds.\n\n\n")
	slow = slow + 2
	t.sleep(3)
	wakeup()

def lookaround():
	start()
	print("You start to feel your way around, noting that the floor is a cold stone, littered with puddles of slimmey water. You feel something furry brush your leg. Are you going to")
	a = input("(A) try to pick it up\n(B) scramble away\n\n")
	if a == "a" or a =="A":
		pickup()
	elif a =="b" or a =="B":
		scramble()
	else:
		print("\nplease enter 'a' or 'b'\n\n\n")
		t.sleep(3)
		lookaround()

def pickup():
	start()
	print("You now have " + str(lives) + " lives")
	t.sleep(slow)
	print("Great job! you've discovered a jacket! This will take away any hypothermia you already have, speeding up your gameplay.")
	slow = 0
	clothing = 1
	move1()
def scramble():
	start()
	print("As you flee the mystery object, you put yous hand down on a course fabric. Quickly you realize that it's a bag. Will it be usefull?")
	a = input("(A) Pick is up! Ill use it.\n(B) I don't want it to slow me down.\n\n")
	if a == "a" or a == "A":
		bag = 3
		move1()
	elif a =="b" or a == "B":
		bag = 0
		move1()
	else:
		print("\nplease enter 'a' or 'b'\n\n\n")
		t.sleep(3)
		scramble()

def move1():
	start()
	print("You feel your way along a wall, as you walk, you feel what seels like a lever on the wall\n")
	a = input("(A Pull it! Twist it! Bop it!\n(B) Hell nah, I'm not touching that!\n\n")
	if a == "a" or a == "A" and clothing == 0:
		print("Why would you pull a rondom lever in a dark hallway????? You're dumb so it opened a trap door into a shollow stream you fell and broke your legs. Now you're slowed by 2 seconds and lost half a life. You can also now only cary two items in your bag.")
		slow = slow + 2
		if bag > 0:
			bag = bag - 1
			lives = 2.5
			stream()
		else:
			print("Why would you pull a rondom lever in a dark hallway????? You're dumb so it opened a trap door into a shollow stream you fell and broke your legs. Since you were wearing a jacket, it absorben a lot of watter, making it impossible to swim. You drowned.")
			lives = 2.5
			stream()
	elif a == "a" or a == "A" and clothing == 1:
		print("Why would you pull a rondom lever in a dark hallway????? You're dumb so it opened a trap door into a shollow stream you fell and broke your legs. Since you were wearing a jacket, it absorben a lot of watter, making it impossible to swim. You drowned. You can also now only cary two items in your bag.")
		slow = slow + 2
		if bag > 0:
			bag = bag - 1
			lives = 2
			stream()
		else:
			print("Why would you pull a rondom lever in a dark hallway????? You're dumb so it opened a trap door into a shollow stream you fell and broke your legs. Since you were wearing a jacket, it absorben a lot of watter, making it impossible to swim. You drowned.")
			lives = 2
			stream()
	elif a =="b" or a == "B":
		print("A good choice, or a missed oportunity? youll never know.")
		move2()
	else:
		print("\nplease enter 'a' or 'b'\n\n\n")
		t.sleep(3)
		move1()

def stream():
	start()
	print("As you wade allong the stream, you can see a flicker of light in the distance. You kick something small inderwater.")
	b = input("(A)Pick it up\n(B)Leave it, I learned my lesson last time\n\n")
	if b == "a" or b == "A":
		if bag > 0:
			bag = bag - 1
			key = "user"
			print("You found a key!")
		else:
			print("You've found a key but have no way to carry it.")
	print("You continue on, determined to find the source of the light.\n\n When you finaly get there, there is a set of stairs reaching upwards back into the darkness, lit by a single ominous torch. Your procede upwards.")
	print("As you reash the top of the stairs there is a door. Will you")
	a = input("(A) try to open the door, and see whats on the other side.\n(B)go back down the stairs, and continue down the stream.\n\n")
	if a == "a" or a == "A":
		if bag > 0:
			print("As you feel the door for a knob, you notice a coil of rope on the back of the door. you put in in your bag and open the door.")
			bag = bag - 1
			hall()
		else:
			print("As you feel the door for a knob, you notice a coil of rope on the back of the door. Unfortunately you have to way to carry it, so you continue on throught the door.")
			hall()
	elif a =="b" or a == "B":
		print("A sudden rush of water knocks you over, and back down the stream to.  you were'nt ablt to breath for two minutes and swollowed a lot of water. You lost half a life.")
		life = life - .5
		if life == 0:
			death()
		else:
			stream()
	else:
		print("\nplease enter 'a' or 'b'\n\n\n")
		t.sleep(3)
		stream()
def hall():
	start()
	print("You continue throught the door into a dimely lit hallway. after a short while, you come to a locked door. How are you going to procede?")
	a = input("(A) Turn around and go back the oposite way throught the hallway\n(B) Go back to the stream...\n\n")
	if a == "a" or a == "A":
		print("After a long walk into the seemingly endless halway that kept getting darker, you arrive back at the lever")
		b = input("(A)Stay at tthe lever\n(B)Keep going back to the start")
		if b == "a" or b == "A":
			move1()
		elif b == "b" or b == "B":
			lookaround()
		else:
			print("\nplease enter 'a' or 'b'\n\n\n")
		t.sleep(3)
		hall()
	elif a == "b" or a == "B":
		stream()

def move2():
	print("You walk down the hallway some more, and ")

	

wakeup()