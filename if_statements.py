# Partner 1: Jackson
# Partner 2: Oleh
''' Instructions:
   Work with a partner to complete these tasks. Assume that all variables are declared; you need only write the if-statement using the variables indicated in the description. Write your solution below the commented description.
'''
 
''' 1. 
   Variable grade is a character. If it is an A, print good work. 
'''
if grade == "a" or grade == "A":
   print("good work")


''' 2. 
   Variable yards is an int. If it is less than 17, multiply yards by 2. 
'''
 
if yards < 17:
  yards = yards * 2
 
''' 3. 
   Variable success is a boolean. If something is a success, print congratulations. 
'''
if success == True :
  print('Congratulations')

 
''' 4. 
   Variable word is a String. If the string's second letter is 'f', print fun. 
'''
if w[1] == "f":
   print("fun")
 
 
''' 5. 
   Variable temp is a float. Variable celsius is a boolean. If celsius is true, convert to fahrenheit, storing the result in temp. F = 1.8C + 32.
'''
if celsius == True :
  temp = temp*1.8 + 32
 
 
''' 6. 
   Variable numItems is an int. Variable averageCost and totalCost are floats. If there are items, calculate the average cost. If there are no items, print no items.
'''
if numItems > 0 :
  averageCost = totalCost/numItems
elif numItems == 0:
  print('No items')

 
 
''' 7. 
   Variable pollution is a float. Variable cutoff is a float. If pollution is less than the cutoff, print safe condition. If pollution is greater than or equal to cutoff, print unsafe condition. 
'''
if pollution < cutoff :
  print('Safe condition')
elif pollution >= cutoff :
  print ('Unsafe condition')
 
 
''' 8. 
   Variable score is a float, and grade is a char. Store the appropriate letter grade in the grade variable according to this chart.
   F: <60; B: 80-89; D: 60-69; A: 90-100; C: 70-79.
'''
if score < 60:
	score = "F"
elif score < 70:
	score = "D"
elif score < 80:
	score = "C"
elif score < 90:
	score = "B"
elif score < 100:
	score = "A"

 
 
''' 9. 
   Variable letter is a char. If it is a lowercase letter, print lowercase. If it is an uppercase, print uppercase. If it is 0-9, print digit. If it is none of these, print symbol.
'''
if letter.islower():
  print('Lowercase')
else:
  if letter.isdigit():
    print('Digit')
  else: 
    print('Uppercase')
 
 
''' 10. 
   Variable neighbors is an int. Determine where you live based on your neighbors.
   50+: city; 25+: suburbia; 1+: rural; 0: middle of nowhere. 
'''
 
if neighbors > 50 :
  print('city')
elif neighbors > 25 : 
  print('suburbia')
elif neighbors == 0 :
  print('middle of nowhere')
 
''' 11. 
   Variables doesSignificantWork, makesBreakthrough, and nobelPrizeCandidate are booleans. A nobel prize winner does significant work and makes a break through. Store true in nobelPrizeCandidate if they merit the award and false if they don't. 
'''
if doesSignificantWork == True and makesBreakthrough == True :
  nobelPrizeCandidate = True
else:
  nobelPrizeCandidate = False


''' 12. 
   Variable tax is a boolean, price and taxRate are floats. If there is tax, update price to reflect the tax you must pay.
'''
if tax == true:
	price = price*(1+taxRate)
 
 
''' 13.  
   Variable word and type are Strings. Determine (not super accurately) what kind of word it is by looking at how it ends. 
   -ly: adverb; -ing; gerund; -s: plural; something else: error   
'''
if word[-1] == 'y' and word[-2] == 'l':
	type = "adverb"
if word[-1] == 'g' and word[-2] == 'n' and word[-3] == 'i':
	type = "gerund"
if word[-1] == 's':
	type = "plural"
else:
	type = "error" 

''' 14. 
   If integer variable currentNumber is odd, change its value so that it is now 3 times currentNumber plus 1, otherwise change its value so that it is now half of currentNumber (rounded down when currentNumber is odd). 
'''

if currentNumber %2 != 0:
	currentNumber = currentNumber*3 + 1

 
''' 15. 
   Assign true to the boolean variable leapYear if the integer variable year is a leap year. (A leap year is a multiple of 4, and if it is a multiple of 100, it must also be a multiple of 400.) 
'''
 
if leapYear %4 == 0:
	if leapYear %100 != 0:
		leapyear = True
	if leapyear %400:
		leapYear = True

 
 
''' 16. 
   Determine the smallest of three ints, a, b and c. Store the smallest one of the three in int result. 
'''
 
if a < b:
	if a < c:
		result = a
	else:
		result = c
elif b < c:
	result = b
else:
	result = c
 
''' 17. 
   If an int, number, is even, a muliple of 5, and in the range of -100 to 100, then it is a special number. Store whether a number is special or not in the boolean variable special. 
'''
 
 
 
''' 18. 
   Variable letter is a char. Determine if the character is a vowel or not by storing a letter code in the int variable code.
   a/e/o/u/i: 1; y: -1; everything else: 0
'''
a_dict = {'a' : int(1), 'e' : int(1), 'o' : int(1), 'u' : int(1), 'i' : int(1), 'y' : int(-1)}

if letter in a_dict:
  if a_dict[letter] == 1:
    print('vowel')
  if a_dict[letter] == -1:
    print('y')
elif letter.isdigit() == True :
  print('digit')
else:
  print('consonant')
 
 
''' 19. 
   Given a string dayOfWeek, determine if it is the weekend. Store the result in boolean isWeekend.
'''
if dayOfWeek == Saturday or dayOfWeek == Sunday:
	isWeekend = True
else:
	isWeekend = False
 
 
''' 20. 
   Given a String variable month, store the number of days in the given month in integer variable numDays. 
'''
if month == April or month == May or month == September or month == November:
	numDays = 30
elif month = February:
	numDays = 29
else:
	numDays = 31
 
''' 21. 
   Three integers, angle1, angle2, and angle3, supposedly made a triangle. Store whether the three given angles make a valid triangle in boolean variable validTriangle.
'''
 if agle1 + angle2 + angle3 == 180:
 	validTriangle = True
 
 
''' 22. 
   Given an integer, electricity, determine someone's monthly electric bill, float payment, following the rubric below. 
   First 50 units: 50 cents/unit
   Next 100 units: 75 cents/unit
   Next 100 units: 1.20/unit
   For units above 250: 1.50/unit, plus an additional 20% surcharge.
'''
if electricity//50 >= 1:
  payment = payment + 0.5*50
  electricity = electricity - 50
  if electricity//100 >=1:
    payment = payment + 0.75*100
    electricity = electricity - 100
    if electricity//100 >=1:
      payment = payment + 1.2*100
      electricity = electricity - 100
      if electricity > 0 :
        payment = 1.5*electricity
        payment = 1.2*payment
        print(payment)
      else:
        print(payment)
    else:
      payment = payment + 1.2*electricity
      print(payment)
  else:
    payment = payment + 0.75*electricity
    print(payment)
else:
  payment = 0.5*electricity
  print(payment)
 
 
''' 23.
   String, greeting, stores a greeting. String language stores the language. If the language is English, greeting is Hello. If the language is French, the greeting is Bonjour. If the language is Spanish, the greeting is Hola. If the language is something else, the greeting is something of your choice.
'''
 
 if language == "English":
 	greeting = "Hello"
 elif language == "French":
 	greeting = "Bonjour"
 elif language == "Spanish":
 	greeting = "Hola"
 else:
 	greeting = "Ni hao"
 
''' 24. 
   Generate a phrase and store it in String phrase, given an int number and a String noun. Here are some sample phrases:
   number: 5; noun: dog; phrase: 5 dogs
   number: 1; noun: cat; phrase: 1 cat
   number: 0; noun: elephant; phrase: 0 elephants
   number: 3; noun: human; phrase: 3 humans
   number: 1; noun: home; phrase: 1 home
'''
phrase = str(number)+' '+noun  
  

''' 25. 
   If a string, userInput, is bacon, print out, "Why did you type bacon?". If it is not bacon, print out, "I like bacon." 
'''

if lower(userInput) == 'bacon':
  print('Why did you type bacon?')
else:
  print('I like bacon.')
 
 
''' 26.
   Come up with your own creative tasks someone could complete to practice if-statements. Also provide solutions.
'''

''' Task 1:

Given a variable 'number' (int), determine whether it has 4 digits or more. If yes, print long number, if no, prcheck if it has '5' in it.
 
'''
 
if len(number) < 4:
	for x in len(number):
		if number[x] == 5:
			print("it) has a five in it")
else:
	print("its a long number")
 
 
 
''' Task 2:
Ask someone thair age, and tell them is thay can vote or not, if they can remind them to go.
 
'''
 
if int(input('how old are you?')) < 18:
 	print("you cant vote yet")
else:
 	print("Make sure to vote this year!")
 
 
 
''' Task 3:
If  booligan rain is true, and the temperature 'temp' is above 32 say its raining if its below say that is's snowing.
 
'''
 
if rain == True:
	if temp >32:
		print("its raining")
	else:
		print("it's snowing")
 else:
 	if temp > 32:
 		print("what a lovely day")
 	else:
 		print("it's cold")
 
 
''' Sources
 http://www.bowdoin.edu/~ltoma/teaching/cs107/spring05/Lectures/allif.pdf
 http://www.codeforwin.in/2015/05/if-else-programming-practice.html
 Ben Dreier for pointing out some creative boolean solutions.
'''