import random as r
lits = []
for i in range (10):
	lits.append(r.randrange(1,101,1))
print(lits)

	
if lits[0] % 3 == 0:
	del lits[0]
elif lits[1] % 3 == 0:
	del lits[1]
elif lits[2] % 3 == 0:
	del lits[2]
elif lits[3] % 3 == 0:
	del lits[3]
elif lits[4] % 3 == 0:
	del lits[4]
elif lits[5] % 3 == 0:
	del lits[5]
elif lits[6] % 3 == 0:
	del lits[6]
elif lits[7] % 3 == 0:
	del lits[7]
elif lits[8] % 3 == 0:
	del lits[8]
elif lits[9] % 3 == 0:
	del lits[9]
elif lits[10] % 3 == 0:
	del lits[10]
print(lits)