import sys
import random as r
board = []
count = 0
bomb = []
gameboard = []
a = 0

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

# ask user for bomb location
#while True:
	#try:
		#x, y = input("Enter a set of coordinates to reveal a square: ").split()

	#except ValueError:
		#print("Type your coordinates x y")
# reveal element at user location
#gameboard[int(x)][int(y)] = board[int(x)-1][int(y)-1]
# print gameboard
#for x in range(0,len(gameboard)-1):
#	print(*gameboard[x])
# while a bomb is not revealed
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
		gameboard[int(x)][int(y)] = board[int(x)][int(y)-1]
	# print gameboard
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
