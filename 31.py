import sys
import random as r
board = []
count = 0
bomb = []



board = [[0]*int(sys.argv[1]) for x in range (int(sys.argv[2]))]
eb = [[0]*int(sys.argv[1]) for x in range (int(sys.argv[2]))]
print(board)

while count < int(sys.argv[3]):
	xrand = r.randrange(0,int(sys.argv[1])-1)
	yrand = r.randrange(0,int(sys.argv[2])-1)
	if xrand and yrand not in bomb:
	#print(xrand,yrand,len(board),len(board[0]))
		board[xrand][yrand] = '*'
		bomb.append(xrand)
		bomb.append(yrand)
		if board[xrand+1][yrand] != '*':
			board[xrand+1][yrand] += 1
		
		if board[xrand-1][yrand] != '*':
			board[xrand-1][yrand] += 1
	
		if board[xrand][yrand+1] != '*':
			board[xrand][yrand+1] += 1
	
		if board[xrand][yrand-1] != '*':
			board[xrand][yrand-1] += 1
	
		if board[xrand+1][yrand+1] != '*':
			board[xrand+1][yrand+1] += 1
	
		if board[xrand+1][yrand-1] != '*':
			board[xrand+1][yrand-1] += 1
	
		if board[xrand-1][yrand+1] != '*':
			board[xrand-1][yrand+1] += 1
	
		if board[xrand-1][yrand-1] != '*':
			board[xrand-1][yrand-1] += 1
	
		count = count+1

print(board,"\n")

for x in range(len(board)):
	print(*board[x])