import random as r
list = []
Round = 0
count = 0
while Round < 1000:
	ticker = 0
	count = 0
	while count < 10:
		x = r.randint(0,1)
		if x == 1:
			ticker += 1
		count += 1
	list.append(ticker)
	Round += 1
print(list.count(0))
print(list.count(1))
print(list.count(2))
print(list.count(3))
print(list.count(4))
print(list.count(5))
print(list.count(6))
print(list.count(7))
print(list.count(8))
print(list.count(9))
print(list.count(10))


