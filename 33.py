# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120
# n! = n*(n-1)*(n-2)*(n-3)...
import sys
n = int(sys.argv[1])

def fact(n):
	if n is 0 or n is 1:
		return 1
	return n*fact(n-1)

fact(n)
print(fact(7))


