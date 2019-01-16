import random as r
import matplotlib.pyplot as plt
a = 0
ticker = 10000
count = 0
lst = []
result = []
while count < ticker:
	x = r.randint(1,8)
	y = r.randint(50,500)
	z = r.randint(1,30)
	a = (x*y*z)
	# print(a)
	lst.append(a)
	count += 1

for x in range(50,120000):
	# print(lst.count(x))
	result.append(lst.count(x))

r = [x for x in range(50,120000)]
plt.bar(r,result)
plt.show()

