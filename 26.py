import random as r
lits = []
first = []
count = 0
for i in range (100):
	lits.append(r.randrange(100,1000,1))
print(lits)
while count < 100:
	first.append(int(str(lits[count])[:1]))
	count = count + 1

first.sort(key = int)

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
count = 0

while count < 100:
	if first[count] == 1:
		one = one + 1
	elif first[count] == 2:
		two = two + 1
	elif first[count] == 3:
		three = three + 1
	elif first[count] == 4:
		four = four + 1
	elif first[count] == 4:
		five = five + 1
	elif first[count] == 6:
		six =six + 1
	elif first[count] == 7:
		seven = seven + 1
	elif first[count] == 8:
		eight = eight + 1
	elif first[count] == 9:
		nine = nine + 1
	count = count + 1

print(first)
print(one  , " ones | ", two , " Twos | ", three , " threes | ", four , " fours | ", five , " fives | ", six , " sixes | \n", seven , " sevens | ", eight , " eights | ", nine , " nines | ")

