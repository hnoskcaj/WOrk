import sys
if 4.85<=float(sys.argv[1])<=5:
	print("You have an A+")
elif 4.7<=float(sys.argv[1]):
	print("You have an A")
elif 4.5<=float(sys.argv[1]):
	print("You have an A-")
elif 4.2<=float(sys.argv[1]):
	print("You have a B+")
elif 3.85<=float(sys.argv[1]):
	print("You have a B")
elif 3.5<=float(sys.argv[1]):
	print("You have a B-")
elif 3.2<=float(sys.argv[1]):
	print("You have a C+")
elif 2.85<=float(sys.argv[1]):
	print("You have a C")
elif 2.5<=float(sys.argv[1]):
	print("You have a C-")
elif 2<=float(sys.argv[1]):
	print("You have a D+")
elif 1.5<=float(sys.argv[1]):
	print("You have a D")
elif 1<=float(sys.argv[1]):
	print("Your have a D-")
elif 0<= float(sys.argv[1]):
	print("You have an F")
else:
	print("Submit a number 0-5")
