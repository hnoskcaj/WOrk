#Jackson Haile 11/12/18

#this code reads an imported csv file, breaks the different inputs into classes, and lets you call them to find information
#about a chamical formula. Type the name of the file you want to import (it should be called "elements.csv"), and run the program.

#Sources: Stacks overflow to find .isnumeric/.isupper functions

#On my honor i have niether given nor recieved unauthorized aid
#-Jackson





#imports file-reader
import csv
#takes file name to input
file = input("Type the file name you want to import here:")
#sets class of elements
class El:
	def __init__(self,name,sym,num,weight,boil,melt):
		#puts variables from the table setup into the elements based on their row and name
		self.name = name
		self.sym = sym
		self.num = num
		self.weight = weight
		self.boil = boil
		self.melt = melt


#create class table
class table:
	def __init__(self):
		self.elems = []
		with open(file) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0
			#goes throgh each spot in the csv and sets the spots to variables
			for z in csv_reader:
				name = z[0] 
				sym = z[2] 
				num = z[1] 
				weight = z[3]
				boil = z[4]
				#tests to see if there is a value at z[5]
				try:
					melt = z[5]
				except IndexError:
					melt = 0
				self.elems.append(El(name,sym,num,weight,boil,melt))

#takes user input and breaks it at the spaces to make a list, x
x= input("\n\nType a chemical formula to find the wieght\n(Put a space between each element and number) \nie: H 2 O\n: ").split()
#sets lists and variables
meltList = 0
boilList = 0
sumList = []
t = table()
result = None
#goes throught the spots in the input
for a in range(0,len(x)):
	#checks that there is somehting to compare
	if a+1<len(x):
		#check to see is a is the whole element(and the next starts and is therefore upercase)
		if x[a+1].isupper():
			#references class elements(El)
			for i in t.elems:
				#if the input matches the symbol
				if x[a] == i.sym:
					#add the weight once becasue the input was only one  part long w/ no number after it
					sumList.append(float(i.weight))
					#adds boiling point
					if boilList < float(i.boil):
						boilList = float(i.boil)
						#adds melting point
					if meltList < float(i.melt):
						meltList = float(i.melt)
			#if the next spot is lower that needs to be included in the symbol
		elif x[a+1].islower():
			#checks to see if there is a number next that references this subsatnce
			if a+2<len(x):
				if x[a+2].isnumeric():
					for i in t.elems:
						#adds the first and second letters of the symbol
						if (x[a]+x[a+1]) == i.sym:
							#multiplies weight my the number of that element
							sumList.append(float(i.weight)*int(x[a+2]))
							#sets boiling point if it is the highest
							if boilList < float(i.boil):
								boilList = float(i.boil)
								#sets as melting point if it is the highest
							if meltList < float(i.melt):
								meltList = float(i.melt)
				#if there is inly one two letter long element
			else:
				for i in t.elems:
					if x[a] == i.sym:
						sumList.append(float(i.weight))
						if boilList < float(i.boil):
							boilList = float(i.boil)
						if meltList < float(i.melt):
							meltList = float(i.melt)
		#is the smbol is one letter long and there is a number following it

		elif x[a+1].isnumeric():
			for i in t.elems:
				if (x[a]) == i.sym:
					sumList.append(float(i.weight)*int(x[a+1]))
					if boilList < float(i.boil):
						boilList = float(i.boil)
					if meltList < float(i.melt):
						meltList = float(i.melt)
 #if the input is only one letter long, then it just adds that with the weight and boiling/melting point
	else:
		for i in t.elems:
				if x[a] == i.sym:
					sumList.append(float(i.weight))
					if boilList < float(i.boil):
						boilList = float(i.boil)
					if meltList < float(i.melt):
						meltList = float(i.melt)
#print out values of total weight, highest boiling point, and highest melting point
#(i was going to try and calculate the actual boiling and melting points, but that ended up being too hard)

print("The attomic weight of this molecule is:",sum(sumList),"\nThe Highest boiling point in this substance is",str(boilList),"\nThe Highest melting point in thes substance is:",str(meltList))