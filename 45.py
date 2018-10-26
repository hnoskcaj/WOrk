class Dog:
	def __init__(self, name):
		self.energy = 5
		self.hunger = 5
		self.weight = 30
		self.happiness = 5
		self.name = name
	#methods - functions
	def eat(self):
		status = ""
		if self.hunger>0:
			self.weight+=1
			self.hunger-=1
			self.energy+=1
			self.happiness +=1
			status = self.name+ "just ate.\n"
		else:
			status = "\nNope, not eating. Not hungry.\n"
		return status

	def stats(self):
		return "Name:"+ self.name+"\nHunger:"+str(self.hunger)+"\nEnergy:"+str(self.energy)+"\nWeight:"+str(self.weight)+"\nHappiness:"+str(self.happiness)+"\n"


myDog = Dog("Oleh")
my2Dog = Dog("Oleh Jr.")
my3Dog = Dog("Oleh the 3rd")
my4Dog = Dog("Oleh the 4rth")
print(my2Dog.stats())
print(my2Dog.eat())
print(my2Dog.stats())