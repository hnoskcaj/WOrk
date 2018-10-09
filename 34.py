import sys
n = int(sys.argv[1])

def fib(n):
	if n is 0 or n is 1 or n is 2:
		return n
	return fib(n-1)+fib(n-2)

print(fib(n))