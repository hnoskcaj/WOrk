
while True:
	try:
		num = int(input("Pick a number between a and 5: "))
		if num<1 or num>5:
			num = int(input("thats not right. Isaid pick a number between 1 and 5: "))
		else:
			print("Success")
	except ValueError:
		print("Yeah, no thats not an integer.")