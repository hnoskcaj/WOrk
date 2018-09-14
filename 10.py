import sys
float(sys.argv[1])
if 4.85<=float(sys.argv[1])<=5:
	print("You have an A+")
elif 4.7<=float(sys.argv[1])<4.85:
	print("You have an A")
elif 4.5<=float(sys.argv[1])<4.7:
	print("You have an A-")
elif 4.2<=float(sys.argv[1])<4.5:
	print("You have a B+")
elif 3.85<=float(sys.argv[1])<4.2:
	print("You have a B")
elif 3.5<=float(sys.argv[1])<3.85:
	print("You have a B-")
elif 3.2<=float(sys.argv[1])<3.5:
	print("You have a C+")
elif 2.85<=float(sys.argv[1])<3.2:
	print("You have a C")
elif 2.5<=float(sys.argv[1])<2.85:
	print("You have a C-")
elif 2<=float(sys.argv[1])<2.5:
	print("You have a D+")
elif 1.5<=float(sys.argv[1])<2:
	print("You have a D")
else:
	print("Submit a number 0-5")
