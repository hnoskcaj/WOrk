import csv

class El:
	def __init__(self,name,sym,num,weight,boil,melt):
		self.name = name
		self.sym = sym
		self.num = num
		self.weight = weight
		self.boil = boil
		self.melt = melt



class table:
	def __init__(self):
		self.elems = []
		with open('elements.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0
			for z in csv_reader:
				name = z[0] 
				sym = z[2] 
				num = z[1] 
				weight = z[3]
				boil = z[4]
				melt = z[4]
				self.elems.append(El(name,sym,num,weight,boil,melt))


x= input("Type a chemical formula to find the wieght: ").split()
meltList = 0
boilList = 0
sumList = []
t = table()
result = None
for a in range(0,len(x)):
	if a+1<len(x):
		if x[a+1].isupper():
			for i in t.elems:
				if x[a] == i.sym:
					sumList.append(float(i.weight))
					if boilList < float(i.boil):
						boilList = float(i.boil)
					if meltList < float(i.melt):
						meltList = float(i.melt)

		elif x[a+1].islower():
			if x[a+2].isnumeric():
				for i in t.elems:
					if (x[a]+x[a+1]) == i.sym:
						sumList.append(float(i.weight)*int(x[a+2]))
						if boilList < float(i.boil):
							boilList = float(i.boil)
						if meltList < float(i.melt):
							meltList = float(i.melt)
			else:
				for i in t.elems:
					if x[a] == i.sym:
						sumList.append(float(i.weight))
						if boilList < float(i.boil):
							boilList = float(i.boil)
						if meltList < float(i.melt):
							meltList = float(i.melt)

		elif x[a+1].isnumeric():
			for i in t.elems:
				if (x[a]) == i.sym:
					sumList.append(float(i.weight)*int(x[a+1]))
					if boilList < float(i.boil):
						boilList = float(i.boil)
					if meltList < float(i.melt):
						meltList = float(i.melt)

	else:
		for i in t.elems:
				if x[a] == i.sym:
					sumList.append(float(i.weight))
					if boilList < float(i.boil):
						boilList = float(i.boil)
					if meltList < float(i.melt):
						meltList = float(i.melt)

print(sum(sumList),"\n"+str(boilList))


# import csv
# with open('elements.csv') as csv_file:
# 	csv_reader = csv.reader(csv_file, delimiter=',')
# 	line_count = 0
# 	for x in csv_reader:
# 			print(x[2])
# 			x[2] = El(x[0],x[1],x[3])
# 			line_count += 1

# summ = 0

# x= input("Type a chemical formula to find the wieght: ").split()
# sumList = []
# print(x[0])
# element = El("H",5,1)
# for a in range(0,len(x)):
# 	if a+1<len(x):
# 		if x[a+1] == int:
# 			sumList.append(x[a].weight)
# 	elif a+2<len(x):
# 		if x[a+2] == int:
# 			sumList.append(x[(a)+(a+1)].weight)
# 	else:
# 		sumList.append(x[0].weight)

# print(sumList)
# for a in range(0,len(sumList)):
# 	summ = summ + sumList[a]

# print(summ)


