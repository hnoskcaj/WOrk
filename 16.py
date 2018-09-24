import time as t
import os
slow = 0
bag = 0
clothing = 0
lives = 3
key = 0
def start():

	os.system('clear')
	global slow, bag, clothing, lives, key
	print("\n\nYou now have " + str(lives) + " lives\n\n")
	t.sleep(slow)
	if lives <= 0:
			death()

def wakeup():
	start()
	print("You wake up in the pitch black dark. You have no idea where you are, or how you got there. The ground is hard, cold and slightly damp.")
	a = input("You are exausted out of your mind, are you going to... \n(A)Go back to sleep\n(B)Get up and feel aroung in the dark\n \n")
	if a == "b" or a == "B":
		lookaround()
	elif a == "a" or a == "A":
		sleep()
	else:
		print("\nplease enter 'a' or 'b'\n\n\n")
		t.sleep(3)
		wakeup()

def sleep():
	global slow
	start()
	print("Congrats, while you were sleeping you fell into a state of hypothermia, now all of your movements and decisions will take an extra 2 seconds.\n\n\n")
	slow = slow + 2
	t.sleep(3)
	wakeup()

def lookaround():
	start()
	print("You start to feel your way around, noting that the floor is a cold stone,\nlittered with puddles of slimmey water. You feel something furry brush your leg.\nAre you going to...")
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
	global slow, clothing
	start()
	print("Great job! you've discovered a jacket! This will take away any hypothermia you\nalready have, speeding up your gameplay.")
	slow = 0
	clothing = 1
	t.sleep(3)
	move1()
def scramble():
	global bag
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
	global slow, bag, lives, clothing
	start()
	print("You feel your way along a wall, as you walk, you feel what seems like a lever on\nthe wall\n")
	a = input("(A) Hell nah, I'm not touching that!\n(B)Pull it! Twist it! Bop it!\n\n\n")
	if a == ("b" or a == "B") and clothing == 0:
		if bag > 0:
			print("Why would you pull a random lever in a dark hallway????? You're dumb so it\nopened a trap door into a shollow stream you fell and broke your legs.\nNow you're slowed by 2 seconds and lost half a life. You can also now only cary two items in your bag.")
			slow = slow + 2
			bag = bag - 1
			lives = lives - .5
			t.sleep(3)
			if input("Hit Enter to procede") == " ":
				stream()
			else:
				stream()
		else:
			print("Why would you pull a random lever in a dark hallway????? You're dumb so it\nopened a trap door into a shollow stream you fell and broke your legs.\nNow you're slowed by 2 seconds and lost half a life.")
			lives = 2.5
			t.sleep(3)
			if input("Hit Enter to procede") == " ":
				stream()
			else:
				stream()
	elif a == ("b" or a == "B") and clothing == 1:
		slow = slow + 2
		if bag > 0:
			print("Why would you pull a random lever in a dark hallway????? You're dumb so it\nopened a trap door into a shollow stream you fell and broke your legs.\nSince you were wearing a jacket, it absorbed a lot of water, making it\nimpossible to swim.\nYou drowned. You can also now only cary two items in your bag.")
			bag = bag - 1
			lives = lives - 1
			t.sleep(3)
			if input("Hit Enter to procede") == " ":
				stream()
			else:
				stream()
		else:
			print("Why would you pull a random lever in a dark hallway????? You're dumb so it\nopened a trap door into a shollow stream you fell and broke your legs.\nSince you were wearing a jacket, it absorbed a lot of water, making it\nimpossible to swim. You drowned.")
			lives = lives - 1
			t.sleep(3)
			if input("Hit Enter to procede") == " ":
				stream()
			else:
				stream()
	elif a =="a" or a == "A":
		print("A good choice, or a missed oportunity? you'll never know.")
		if input("Hit Enter to procede") == " ":
			move2()
		else:
			move2()

	else:
		print("\nplease enter 'a' or 'b'\n\n\n")
		t.sleep(3)
		move1()

def stream():
	global bag, key, lives
	start()
	if key == 0:
		print("As you wade along the stream, you can see a flicker of light in the distance.\nYou kick something small underwater.")
		b = input("(A)Pick it up\n(B)Leave it, I learned my lesson last time\n\n")
		if b == "a" or b == "A":
			if bag > 0:
				bag = bag - 1
				key = 1
				print("You found a key!")
				t.sleep(3)
			else:
				print("You've found a key but have no way to carry it. If only you had a bag... maybe\nthere was one by the sart???\n\n")
				
		elif b == "b" or b == "B":
			pass
		else:
			print("\nplease enter 'a' or 'b'\n\n\n")
			t.sleep(3)
			stream()

	else:
		print("As you wade allong the stream, you can see a flicker of light in the distance.")
	
	print("You continue on, determined to find the source of the light.\n\nWhen you finaly get there, there is a set of stairs reaching upwards back into the darkness, lit by a single ominous torch. You procede upwards.")
	print("As you reach the top of the stairs there is a door. Will you")
	a = input("(A)Go back down the stairs, and continue down the stream.\n(B)Try to open the door, and see whats on the other side.\n\n")
	if a == "b" or a == "B":
		if bag > 0:
			print("As you feel the door for a knob, you notice a coil of rope on the back of the\ndoor. you put in in your bag and open the door.\nYou continue throught the door into a dimely lit hallway.")
			bag = bag - 1
			if input("Hit Enter to procede") == " ":
				hall()
			else:
				hall()
	
		else:
			print("As you feel the door for a knob, you notice a coil of rope on the back of the\ndoor. Unfortunately you have to way to carry it, so you continue on throught the door. \nYou continue throught the door into a dimely lit hallway.")
			t.sleep(3)
			if input("Hit Enter to procede") == " ":
				hall()
			else:
				hall()
	elif a =="a" or a == "A":
		print("A sudden rush of water knocks you over, and back down the stream.\nYou were'nt able to breath for two minutes and swollowed a lot of water.\nYou lost half a life.")
		lives = lives - .5
		if lives == 0:
			death()
		else:
			if input("Hit Enter to procede") == " ":
				stream()
			else:
				stream()
	else:
		print("\nplease enter 'a' or 'b'\n\n\n")
		t.sleep(3)
		stream()
def hall():
	start()
	if key == 0:
		print("After a short while, you come to a locked door. How are you going to procede?")
		a = input("(A) Turn around and go back the oposite way throught the hallway\n(B) Go back to the door in the hall...\n\n")
		if a == "a" or a == "A":
			print("After a long walk into the seemingly endless halway that kept getting darker, you arrive back at the lever")
			b = input("(A)Stay at the lever\n(B)Keep going back to the start\n\n")
			if b == "a" or b == "A":
				move1()
			elif b == "b" or b == "B":
				lookaround()
			else:
				print("\nplease enter 'a' or 'b'\n\n\n")
				t.sleep(3)
				hall()
		elif a == "b" or a == "B":
			door()
		else:
			print("\nplease enter 'a' or 'b'\n\n\n")
			t.sleep(3)
			hall()
	elif key == 1:
		print("After a short while, you come to a locked door. How are you going to procede?")
		a = input("(A) Turn around and go back the oposite way throught the hallway\n(B) Go back to the stream...\n(C)Use the key I found.\n\n")
		t.sleep(3)
		if a == "a" or a == "A":
			print("After a long walk into the seemingly endless halway that kept getting darker, you arrive back at the lever")
			b = input("(A)Stay at tthe lever\n(B)Keep going back to the start\n\n")
			t.sleep(3)
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
		elif a == "c" or a =="C":
			print("You use the key that you found earlier. Cautiously open the door, and step out\nonto a city street.\nYou've escaped this underground dungeon, but will you get home? good luck!")
			exit()
		else:
			print("\nplease enter 'a' or 'b'\n\n\n")
			t.sleep(3)
			hall()
		
def move2():
	global lives
	start()
	print("You walk down the hallway some more and, as there seems to be more light the further you go, pass by a doorway.")
	a = input("(A)Go throught the door\n(B) keep going down the hallway\n\n")
	if a == "a" or a == "A":
		door()
	elif a =="b" or a == "B":
		hall()
	else:
		print("\nplease enter 'a' or 'b'\n\n\n")
		t.sleep(3)
		move2()

def death():
	os.system('clear')
	print("\n\nYou now have " + str(lives) + " lives\n\n")
	print("You Died XD!")

def door():
	global lives
	start()
	print("You go throught the door which leads to a set of steps. as you walk down, you\nslip. Falling to the bottom into a stream. After being tumbled in the water,\nyour dead body ends up at the base of the stream.\n")
	lives = lives - 1
	t.sleep(3)
	if input("Hit Enter to procede") == " ":
		stream()
	else:
		stream()
	

wakeup()