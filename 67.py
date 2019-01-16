import random as r
import math as m
import matplotlib.pyplot as plt
ticker = 100
count = 0
result = []
lst = []
while count < ticker:
	x = r.randint(1,6)
	if x == 1:
		f = r.randint(0,int(3500/9))
		p = r.randint(0,int((3500-int(f)*9)/4))
		c = r.randint(0,int((3500-int(f)*9-int(p)*4)/4))
	if x == 2:
		f = r.randint(0,int(3500/9))
		c = r.randint(0,int((3500-int(f)*9)/4))
		p = r.randint(0,int((3500-int(f)*9-int(c)*4)/4))
	if x == 3:
		p = r.randint(0,int(3500/4))
		f = r.randint(0,int((3500-int(p)*4)/9))
		c = r.randint(0,int((3500-int(f)*9-int(p)*4)/4))
	if x == 4:
		p = r.randint(0,int(3500/4))
		c = r.randint(0,int((3500-int(p)*4)/4))
		f = r.randint(0,int(3500-int(c)*4-int(p)*4/9))
	if x == 5:
		c = r.randint(0,int(3500/4))
		p = r.randint(0,int((3500-int(c)*4)/4))
		f = r.randint(0,int((3500-int(c)*4-int(p)*4)/9))
	if x == 6:
		c = r.randint(0,int(3500/4))
		f = r.randint(0,int((3500-int(c)*4)/9))
		p = r.randint(0,int((3500-int(f)*9-int(c)*4)/4))
	cal = f*9+p*4+c*4
	lst.append(cal)
	count += 1
for x in range(1750,3500):
	# print(lst.count(x))
	result.append(lst.count(x))

r = [x for x in range(1750,3500)]
plt.bar(r,result)
plt.show()
