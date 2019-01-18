import random as r
import math as m
import matplotlib.pyplot as plt
ticker = 1000
count = 0
result = []
lst = []
lit = []
while count < ticker:
	x = r.randint(1,6)
	if x == 1:
		f = r.randint(0,int(3500))
		p = r.randint(0,int((3500-int(f))))
		c = r.randint(0,int((3500-int(f)-int(p))))
	if x == 2:
		f = r.randint(0,int(3500))
		c = r.randint(0,int((3500-int(f))))
		p = r.randint(0,int((3500-int(f)-int(c))))
	if x == 3:
		p = r.randint(0,int(3500))
		f = r.randint(0,int((3500-int(p))))
		c = r.randint(0,int((3500-int(f)-int(p))))
	if x == 4:
		p = r.randint(0,int(3500))
		c = r.randint(0,int((3500-int(p))))
		f = r.randint(0,int((3500-int(c)-int(p))))
	if x == 5:
		c = r.randint(0,int(3500))
		p = r.randint(0,int((3500-int(c))))
		f = r.randint(0,int((3500-int(c)-int(p))))
	if x == 6:
		c = r.randint(0,int(3500))
		f = r.randint(0,int((3500-int(c))))
		p = r.randint(0,int((3500-int(f)-int(c))))
	cal = f+p+c
	lst.append(cal)
	count += 1
	lit.append(x)
for x in range(0,3500):
	# print(lst.count(x))
	result.append(lst.count(x))

r = [x for x in range(0,3500)]
plt.bar(r,result)
plt.show()


for x in range(0,7):
	# print(lst.count(x))
	result.append(lit.count(x))

r = [x for x in range(0,7)]
plt.bar(r,result)
plt.show()

print(r,result)
