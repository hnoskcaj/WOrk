class El:
	def __init__(self,name,num,weight):
		self.name = name
		self.num = num
		self.weight = weight


import csv
with open('elements.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for x in csv_reader:
			print(x[2])
			x[2] = El(x[0],x[1],x[3])
			line_count += 1

summ = 0

x= input("Type a chemical formula to find the wieght: ").split()
sumList = []
print(x[0])
element = El("H",5,1)
for a in range(0,len(x)):
	if a+1<len(x):
		if x[a+1] == int:
			sumList.append(x[a].weight)
	elif a+2<len(x):
		if x[a+2] == int:
			sumList.append(x[(a)+(a+1)].weight)
	else:
		sumList.append(x[0].weight)

print(sumList)
for a in range(0,len(sumList)):
	summ = summ + sumList[a]

print(summ)


