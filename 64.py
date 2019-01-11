import random as r
a = 0
z = 100000000
count = 0
while count < z:
	x = r.uniform(0,4)
	if x <= 3.14:
		a += 1
	count += 1
print(a)
print(a*4/z)