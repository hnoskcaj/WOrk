import sys


def count(n):
	global b, a, X
	if a[b] == 'x':
		X = X+1
	if b == len(str(a)):
		return
	b = b +1

count(n)
print(X)
	
