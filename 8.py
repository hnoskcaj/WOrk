import sys
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])
h = y- (14-m)/12
i = h + h/4 - h/100 + h/400
j = m + 12 * ((14 - m)//12) - 2
k = (d + i + (31*j)/12)%7
l = round(k)
print(l)
