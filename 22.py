sevens = []
while count<700:
	sevens.append(count)
	count += 7
lits = [x * x for x in sevens]
print(lits)