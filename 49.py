import csv
with open('elements.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for x in csv_reader:
			{x[2]} = El({x[0]},{x[1]} ,{x[3]},)
			line_count += 1
	

class El:
	def __init__(self,name,num,weight):
		self.name = name
		self.num = num
		self.weight = weight

	def stats(self):
		return "Name:"+ self.name+"\nAtomic Number:"+str(self.num)+"\nAtomic weight:"+str(self.wieght)


x= input("Type a chemical formula to find the wieght: ").split()

for a in len(x):
	if sys.argv[a+1] = int:
		sys.argv[a].stats()

