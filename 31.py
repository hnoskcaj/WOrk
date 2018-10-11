import sys
import random as r
board = []
count = 0
bomb = []
gameboard = []
a = 0
clear = []
zeros = 0

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

print(width, height)

for x in range(0,len(gameboard)-1):
	for b in range(1,height-1):
		gameboard[b][0] = b
	gameboard[x][0]
	del gameboard[x][-1]
	for a in range(1,width-1):
		gameboard[0][a]= a
	
	print(*gameboard[x])

# def reveal():
# 	global xx, yy, x, y, zeros, width, height
# 	zeros = 8
# 	while zeros > 0:
# 		print(clear)
# 		clear.append((xx,yy))
# 		for z in range(len(clear)):
# 			xx = clear[z][0]
# 			yy = clear[z][1]
# 			print (clear)
# 			for down in range(-1,2):
# 				for over in range(-1,2):
# 					if 0 < xx+over < width-1 and 0 < yy+down < height-1:
# 						gameboard[xx+over][yy+down] = board[xx+over][yy+down-1]
# 						if gameboard[xx+over][yy+down] == 0:
# 							if (xx+over,yy+down) not in clear:
# 								clear.append((xx+over,yy+down))
# 								zeros = zeros + 7
# 						else:
# 							zeros = zeros-1
# 					else:
# 						zeros = zeros-1

def reveal():
	global xx, yy, x, y, zeros, width, height
	clear.append((xx,yy))

	z = 0
	while len(clear) > z:
		# print(clear)
		
		xx = clear[z][0]
		yy = clear[z][1]
		# print (clear)
		for down in range(-1,2):
			for over in range(-1,2):
				if 0 < xx+over < width-1 and 0 < yy+down < height-1:
					gameboard[xx+over][yy+down] = board[xx+over][yy+down-1]
					if gameboard[xx+over][yy+down] == 0:
						if (xx+over,yy+down) not in clear:
							clear.append((xx+over,yy+down))
		z+=1
		 


			# if  0 < xx < 10 and 0 < yy-1 < 10 and board[xx-1][yy] != '*':
			# 	gameboard[xx][yy+1] = board[xx-1][yy]
			# 	if gameboard[xx][yy+1] == 0:
			# 		if (xx,yy+1) not in clear:
			# 			clear.append((xx,yy+1))
			# 			zeros = zeros + 8
			# 	else:
			# 		zeros = zeros-1
			# else:
			# 		zeros = zeros-1

		
			# if 0 < xx-1 < 10 and 0 < yy-2 < 10 and board[xx-1][yy-2] != '*':
			# 	gameboard[xx][yy-1] = board[xx-1][yy-2]
			# 	if gameboard[xx][yy-1] == 0:
			# 		if (xx,yy-1) not in clear:
			# 			clear.append((xx,yy-1))
			# 			zeros = zeros + 8
			# 	else:
			# 		zeros = zeros-1
			# else:
			# 	zeros = zeros-1

			# if 0 < xx < 10 and 0 < yy-1 < 10 and board[xx][yy-1] != '*':
			# 	gameboard[xx+1][yy] = board[xx][yy-1]
			# 	if gameboard[xx+1][yy] == 0:
			# 		if (xx+1,yy) not in clear:
			# 			clear.append((xx+1,yy))
			# 			zeros = zeros + 8
			# 	else:
			# 		zeros = zeros-1
			# else:
			# 		zeros = zeros-1

			# if 0 < xx < 10 and 0 < yy < 10 and board[xx][yy] != '*':
			# 	gameboard[xx+1][yy+1] = board[xx][yy]
			# 	if gameboard[xx+1][yy+1] == 0:
			# 		if (xx+1,yy+1) not in clear:
			# 			clear.append((xx+1,yy+1))
			# 			zeros = zeros + 8
			# 	else:
			# 		zeros = zeros-1
			# else:
			# 	zeros = zeros-1
	
			# if 0 < xx < 10 and 0 < yy-2 < 10 and board[xx][yy-2] != '*':
			# 	gameboard[xx+1][yy-1] = board[xx][yy-2]
			# 	if gameboard[xx+1][yy-1] == 0:
			# 		if (xx+1,yy-1) not in clear:
			# 			clear.append((xx+1,yy-1))
			# 			zeros = zeros + 8
			# 	else:
			# 		zeros = zeros-1
			# else:
			# 		zeros = zeros-1

			# if 0 < xx-2 < 10 and 0 < yy < 10 and board[xx-2][yy] != '*':
			# 	gameboard[xx-1][yy+1] = board[xx-2][yy]
			# 	if gameboard[xx-1][yy+1] == 0:
			# 		if (xx-1,yy+1) not in clear:
			# 			clear.append((xx-1,yy+1))
			# 			zeros = zeros + 8
			# 	else:
			# 		zeros = zeros-1
			# else:
			# 		zeros = zeros-1
			# if 0 < xx-2 < 10 and 0 < yy-1 < 10 and board[xx-2][yy-1] != '*':
			# 	gameboard[xx-1][yy] = board[xx-2][yy-1]
			# 	if gameboard[xx-1][yy] == 0:
			# 		if (xx-1,yy) not in clear:
			# 			clear.append((xx-1,yy))
			# 			zeros = zeros + 8
			# 	else:
			# 		zeros = zeros-1
			# else:
			# 		zeros = zeros-1
		
			# if 0 < xx-2 < 10 and 0 < yy-2 < 10 and board[xx-2][yy-2] != '*':
			# 	gameboard[xx-1][yy-1] = board[xx-2][yy-2]
			# 	if gameboard[xx-1][yy-1] == 0:
			# 		if (xx-1,yy-1) not in clear:
			# 			clear.append((xx-1,yy-1))
			# 			zeros = zeros + 8
			# 	else:
			# 		zeros = zeros-1
			# else:
			# 		zeros = zeros-1
	







x = 0
y = 0
while True:
	try:
		if gameboard[int(x)][int(y)] == '*':
			break
	# choose second location
		x, y, w = input("Enter a set of coordinates to reveal a square, add an extra 1 at the end to flag or unflag it: ").split()
	# reveal location
		print(x,y)
		xx = int(x)
		yy = int(y)
		if w == 1:
			if gameboard[int(x)][int(y)] != '#':
				gameboard[int(x)][int(y)] = '#'
	
		elif board[int(x)][int(y)-1] == 0:
			reveal()

		gameboard[int(x)][int(y)] = board[int(x)][int(y)-1]
	# print gameboard
		for a in range(1,width-1):
			gameboard[0][a]= a
		for b in range(1,height-1):
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
