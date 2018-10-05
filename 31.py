#https://stackoverflow.com/questions/961263/two-values-from-one-input-in-python
#Accessed on 10/3/18 referenced a way to pull arguments from an input

import sys
import random as r
board = []
count = 0
bomb = []
gameboard = []
a = 0
clear = []

width = int(sys.argv[1])+2 
height = int(sys.argv[2])+2

gameboard = [['-']*(width) for x in range (height)]

board = [[0]*width for x in range (height)]
print(board)

while count < int(sys.argv[3]):
	xrand = r.randrange(1,height-1)
	yrand = r.randrange(1,width-1)

	#a = xrand + yrand
	if (xrand,yrand) not in bomb:
	#print(xrand,yrand,len(board),len(board[0]))
		board[xrand][yrand] = '*'
		bomb.append((xrand,yrand))
		#bomb.append(yrand)
		print(xrand,yrand,"---------")

		if board[xrand][yrand+1] != '*':
			board[xrand][yrand+1] += 1
	
		if board[xrand][yrand-1] != '*':
			board[xrand][yrand-1] += 1


		if board[xrand+1][yrand] != '*':
			board[xrand+1][yrand] += 1
	
		if board[xrand+1][yrand+1] != '*':
			board[xrand+1][yrand+1] += 1
	
		if board[xrand+1][yrand-1] != '*':
			board[xrand+1][yrand-1] += 1


	
		if board[xrand-1][yrand+1] != '*':
			board[xrand-1][yrand+1] += 1

		if board[xrand-1][yrand] != '*':
			board[xrand-1][yrand] += 1
	
		if board[xrand-1][yrand-1] != '*':
			board[xrand-1][yrand-1] += 1
	
		count = count+1

print(board,"\n")

for x in range(1,len(board)-1):
	del board[x][0]
	del board[x][-1]
	print(*board[x])

print("\n")



for x in range(0,len(gameboard)-1):
	for b in range(1,11):
		gameboard[b][0] = b
	gameboard[x][0]
	del gameboard[x][-1]
	for a in range(1,11):
		gameboard[0][a]= a
	
	print(*gameboard[x])

def reveal():
	global xx, yy, x, y
	print(xx,yy)
	for z in range(len(clear)):
			xx = clear[z][1]
			yy = clear[z][2]

	gameboard[int(x)][int(y)+1] = board[xx][yy+1]
	if board[xx][yy+1] == 0:
		clear.append((xx,yy+1))

	
	gameboard[int(x)][int(y)-1] = board[xx][yy-1]
	if board[xx][yy-1] == 0:
		clear.append((xx,yy-1))


	gameboard[int(x)+1][int(y)] = board[xx+1][yy]
	if board[xx+1][yy] == 0:
		clear.append((xx+1,yy))

	
	gameboard[int(x)+1][int(y)+1] = board[xx+1][yy+1]
	if board[xx+1][yy+1] == 0:
		clear.append((xx+1,yy+1))

	
	gameboard[int(x)+1][int(y)-1] = board[xx+1][yy-1]
	if board[xx+1][yy-1] == 0:
		clear.append((xx+1,yy-1))

	
	gameboard[int(x)-1][int(y)+1] = board[xx-1][yy+1]
	if gameboard[xx-1][yy+1] == 0:
		clear.append((xx-1,yy+1))


	gameboard[int(x)-1][int(y)] = board[xx-1][yy]
	if gameboard[xx-1][yy] == 0:
		clear.append((xx-1,yy))

	
	gameboard[int(x)-1][int(y)-1] = board[xx-1][yy-1]
	if gameboard[xx-1][yy-1] == 0:
		clear.append((xx-1,yy-1))





x = 0
y = 0
while True:
	try:
		if gameboard[int(x)][int(y)] == '*':
			break
	# choose second location
		x, y = input("Enter a set of coordinates to reveal a square: ").split()
	# reveal location
		print(x,y)
		xx = int(x)-1
		yy = int(y)-1
		if board[int(x)-1][int(y)-1] == 0:
			reveal()

		gameboard[int(x)][int(y)] = board[int(x)-1][int(y)-1]
	# print gameboard
		for a in range(1,11):
			gameboard[0][a]= a
		for b in range(1,11):
			gameboard[b][0] = b

		for a in range(0,len(gameboard)-1):
			print(*gameboard[a])
	except ValueError:
		print("Type your coordinates x y")

# for x in range(0,len(gameboard)-1):
# 		print(*gameboard[x])
print("You clicked on a bomb!")
exit()

#guess = input("Enter a set of coordinates to reveal a square!")
#print(guess.arg[1])




