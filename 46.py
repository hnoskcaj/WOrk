# #balance
# acound number
# username/password

# check balance
# deposit/withdraw
# login/out
an = 0
import random

def new():
	global an
	an = random.randint(0,10000)
	print("your acount number is\n", an)

class bank:
	def __init__(self, an):
		self.balance = 0
		self.acountNumber = an

	def withdraw(self,x):
		self.balance -= x
		print(self.balance)
	def deposit(self,x):
		self.balance += x
		print(self.balance)

new()
an = bank(an)
an.withdraw(50)