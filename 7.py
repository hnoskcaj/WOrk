import sys
x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]
if x<y<z or x>y>z:
	print("true")
else:
	print("false")