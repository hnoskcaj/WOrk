import random as r
lits = []
first = []
for i in range (6):
	lits.append(r.randrange(1,271,13))
print(lits)
print(int(str(lits[0])[:1]))
