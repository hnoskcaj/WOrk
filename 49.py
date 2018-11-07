class El:
	def __init__(self,name,num,weight):
		self.name = name
		self.num = num
		self.weight = weight

	def weights(self):
		return self.wieght


import csv
with open('elements.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for x in csv_reader:
			x[2] = El(x[0],x[1],x[3])
			line_count += 1



x= input("Type a chemical formula to find the wieght: ").split()
sumList = []
for a in range(0,len(x)):
	if sys.argv[a+1] == int:
		sumList.append(sys.argv[a].weights())
	elif sys.argv[a+2] == int:
		sumList.append(sys.argv[(a)+(a+1)].weights())

