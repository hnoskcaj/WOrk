import sys
fib1 = 1
fib2 = 1
count = int(sys.argv[1])
print("1\n1")
count = count -2
while count > 0:
	fib2 = fib1 + fib2
	print(fib2)
	count = count - 1
	if count > 0:
		fib1 = fib1 + fib2
		print(fib1)
		count = count - 1
	else: exit()