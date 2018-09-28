import random as r
lits = []
first = []
count = 0
for i in range (100):
	lits.append(r.randrange(100,1000,1))
print(lits)
while count < 100:
	first.append(int(str(lits[count])[:1]))
	count = count + 1
#first.append(int(str(lits[1])[:1]))
#first.append(int(str(lits[2])[:1]))
#first.append(int(str(lits[3])[:1]))
#first.append(int(str(lits[4])[:1]))
#first.append(int(str(lits[5])[:1]))

print(first)

