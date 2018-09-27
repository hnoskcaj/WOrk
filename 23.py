import random

def sum_num(number):
 number = str(number)
 summa = 0
 for i in range(len(number)):
  summa = summa + int(number[i])
 return summa

a = random.sample(range(100), 50)
b = []
for i in range(len(a)):
 number = a[i]
 if sum_num(number) == 5 :
  b.append(number)
print(a)
print(b)