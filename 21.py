import sys
end = sys.argv[1]
count = 0

#while int(end) > int(count):
	#print(7*int(count))
	#count = count + 1

sevens = [x for x in range(0,700,7)]
print(sevens, len(sevens))

sevens = []
while count<700:
	sevens.append(count)
	count += 7
lits = [x * x for x in sevens]
print(lits)