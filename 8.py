import sys
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])
h = y- (14-m)/12
i = h + h/4 - h/100 + h/400
j = m + 12 * ((14 - m)//12) - 2
k = (d + i + (31*j)/12)%7
l = round(k)
if l == 0:
	print("Sunday")
else:
		if l == 1:
			print("Monday")
		else:
			if l == 2:
				print("Tuesday")
			else:
				if l == 3:
					print("Wednesday")
				else:
					if l == 4:
						print("Thursday")
					else:
						if l == 5:
							print("Friday")
						else:
							if l == 6:
								print("Saturday")

