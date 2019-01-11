import random as r
import matplotlib.pyplot as plt

List = []
Round = 0
count = 0
result = []

while Round < 1000:
	ticker = 0
	count = 0
	while count < 10:
		x = r.randint(0,1)
		if x == 1:
			ticker += 1
		count += 1
	List.append(ticker)
	Round += 1

print(List.count(0))
print(List.count(1))
print(List.count(2))
print(List.count(3))
print(List.count(4))
print(List.count(5))
print(List.count(6))
print(List.count(7))
print(List.count(8))
print(List.count(9))
print(List.count(10))


result.append(List.count(0))
result.append(List.count(1))
result.append(List.count(2))
result.append(List.count(3))
result.append(List.count(4))
result.append(List.count(5))
result.append(List.count(6))
result.append(List.count(7))
result.append(List.count(8))
result.append(List.count(9))
result.append(List.count(10))

r = [x for x in range(11)]
print(result)
plt.bar(r,result)
plt.show()