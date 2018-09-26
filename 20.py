a = []

a +=[2]
a.append(4)
a.append(7)
a.append(1)
a.append(3)
a += [2,1,2,3,4,5]

print(a)

a[4] = 7

print(a)

#remove 1 through 4 form the list

del a[1:5]

print(a)

print(a.pop(2))

a.remove(a[3])
print(a)

print(a[-2])

#swap
a = 1
b = 2
temp = a
a = b
b = temp

#or
a,b = 1,5
print(a,b)
a,b = b,a
print(a,b)