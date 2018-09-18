def start():
	response = input("Greatings! \n\nyou are lookign for treasure. your map says that the treasure can be found northerly. However your friend says he heard the treasure can be found in the south. \n\nDo you 1) trust your friend, or 2) trust the map? ")
	if response == "1":
		friend()
	elif response == '2':
		map()
	else:
		start()

def map():
	print("you drowned ;(")
	game = (input("Do you want to play again? ")).lower()
	if game == "yes":
		start()
	else:
		exit()
def friend():
	pass

start()