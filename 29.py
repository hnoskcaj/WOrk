import sys
import random as r
board = []
eb = []
count = 0
x = 0
y = 0


board = [[0]*int(sys.argv[1]) for x in range (int(sys.argv[2]))]
eb = [[0]*int(sys.argv[1]) for x in range (int(sys.argv[2]))]
print(board)

while count < int(sys.argv[3]):
	board[r.randrange(0,int(sys.argv[1]))][r.randrange(0,int(sys.argv[2]))] = 1
	count = count+1

print(board)


#for x, y in zip(range(int(sys.argv[1]))), zip(range(int(sys.argv[2]))):
#while x<= int(sys.argv[1]) and y <= int(sys.argv[2]):
	#if board[1][3] ==1:
	#	eb[x][y] = '*'
	#	x = x + 1
	#	y = y + 1

for x in range(len(board)):
	print(*board[x])

#for x, y in zip(range(int(sys.argv[1]))), zip(range(int(sys.argv[2]))):
while x<= 5 and y <= 5:
	if board[x][y] ==1:
		eb[x][y] = '*'
	x = x + 1
	y = y + 1

print("\n\n")

for x in range(len(eb)):
	print(*eb[x])

