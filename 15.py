
def guess():
	global List
	x = input("number_")
	if x == 5:
		print("yes")
	else:
		List = List + x
		print(List)

x = input("number_")
if x == 5:
	print("yes")
else:
	List = x
	print(List)
	guess()