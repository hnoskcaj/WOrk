class Card:
	def __init__(self,rank,suit):
		self.rank = rank
		self.suit = suit
	def disp(self):
		print(self.rank, self.suit)
class Deck:
	def __init__(self):
		Suits = ["h","d","c","s"]
		for i in Suits:
			for x in range(1,14):
				self.cards.append(Card(i,x))

dec = Deck()

