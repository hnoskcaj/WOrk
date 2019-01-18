
# Matplotlib project
# 1/17/18

#on my honor i have neither given nor revieved unauthorized aid -Jackson haile

# Calculate the calories and macros if you ramdomely eat macros up to 3500 calories.
#Eat the proteinup to 3500, then calories  of the remailing calls,
#then fat of the remaining cals.

#--------------------------------------------------------------------
#import modules
import random as r
import math as m
import matplotlib.pyplot as plt
#set total reps
ticker = 1000
count = 0
result = []
lst = []
lit = []
prot = []
fat = []
carb = []
#for ticker number times...
while count < ticker:
	#randomely chooses which order to pick macros(protein, fat, carbs) in
	x = r.randint(1,6)
	if x == 1:
		#chooses random amount in grames from total calories
		f = r.randint(0,int(3500/9))
		#chooses random second value ( in grams) out of remaining calories
		p = r.randint(0,int((3500-int(f)*9)/4))
		#chooses third random value again in grams from the remaining callories
		c = r.randint(0,int((3500-int(f)*9-int(p)*4)/4))
		#the same for the other five orders
	if x == 2:
		f = r.randint(0,int(3500/9))
		c = r.randint(0,int((3500-int(f)*9)/4))
		p = r.randint(0,int((3500-int(f)*9-int(c)*4)/4))
	if x == 3:
		p = r.randint(0,int(3500/4))
		f = r.randint(0,int((3500-int(p)*4)/9))
		c = r.randint(0,int((3500-int(f)*9-int(p)*4)/4))
	if x == 4:
		p = r.randint(0,int(3500/4))
		c = r.randint(0,int((3500-int(p)*4)/4))
		f = r.randint(0,int((3500-int(c)*4-int(p)*4)/9))
	if x == 5:
		c = r.randint(0,int(3500/4))
		p = r.randint(0,int((3500-int(c)*4)/4))
		f = r.randint(0,int((3500-int(c)*4-int(p)*4)/9))
	if x == 6:
		c = r.randint(0,int(3500/4))
		f = r.randint(0,int((3500-int(c)*4)/9))
		p = r.randint(0,int((3500-int(f)*9-int(c)*4)/4))
		#multiplies grams of macros by cal per gram, and adds together
	cal = f*9+p*4+c*4
	prot.append(p)
	fat.append(f)
	carb.append(c)
	lst.append(cal)
	count += 1

for x in range(0,3500):
	#counts the nuber of times each value accures in total repititions
	result.append(lst.count(x))

r = [x for x in range(0,3500)]
#print out chats of results
plt.bar(r,result)
plt.title("Calories")
plt.show()

########################################
result = []
for x in range(0,875):
	#counts the nuber of times each value accures in total repititions
	result.append(prot.count(x))

r = [x for x in range(0,875)]
#print out chats of results
plt.bar(r,result)
plt.title("Protein")
plt.show()

########################################
result = []
for x in range(0,875):
	#counts the nuber of times each value accures in total repititions
	result.append(carb.count(x))

r = [x for x in range(0,875)]
#print out chats of results
plt.bar(r,result)
plt.title("Carbs")
plt.show()

########################################
result = []
for x in range(0,389):
	#counts the nuber of times each value accures in total repititions
	result.append(fat.count(x))

r = [x for x in range(0,389)]
#print out chats of results
plt.bar(r,result)
plt.title("Fat")
plt.show()

print(r,result)
