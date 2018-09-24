import sys
fib = 1
count = int(sys.argv[1])
print(type(count))
while count > 0:
	fib = fib + 1
	print(fib)
	count = count - 1