# Python Library project.
# Jackson Haile
# 1/19
# On myhonor i have neither given nor recieved unuthorized aid -Jackson

# sources: Kivy docs, stacks overflow, python docs, Alexander Taylor (youtube.com/watch?v=F7UKmK9eQLY)

# Kivy: https://kivy.org/#home





############################################################################

#Basic Button

# in this program, we create a button with the text "start", and set a back ground color. the button is not
# linked to anything, so when it is clicked, it simply briefly changes color to register the click.

import kivy
from kivy.app import App
from kivy.uix.button import Button

#set up the button class
class Book(App):
	def build(self):
		#creating button properties, the text wil say "start", the color is set to (3,3,1,1),
		#and the font size is set to 100
		return Button(text = "Start", background_color=(3,3,1,1), font_size=100)
		
#run the app for button
if __name__ == "__main__":
	Book().run()

############################################################################

#Interactive Button

# In this program, we create a button that can be moved around with our cursour, and can be rotated by
# holding with two fingers on a ytough device, or option right clicking on a computer at two points.

import kivy
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
#create class
class Book(App):
	def build(self):
		f = FloatLayout()
		s = Scatter()
		# Set button labels
		l = Label(text = "Hello world", font_size = 150)

		#add scatter and float properties to button widget
		f.add_widget(s)
		s.add_widget(l)
		return f
#run program
Book().run()


############################################################################
#Binding a function to the button

# In this program, we create a button that is bound with a function, menaing that when th ebutton is clicked,
# it will run that function.

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

#button class
class Book(Button):
	#creating button setup
	def __init__(self,**kwargs):
		super(Book, self).__init__(**kwargs)
		#button properties, the same as before, but nor we are adding position in the window witht he
		#command pos=(650,450)
		btn1 = Button(pos=(650,450),size = (300,300),text = "Red", background_color=(1,7,1,1), font_size=100)
		#binding the button with the function defined below "red"
		btn1.bind(on_press=self.red)
		self.add_widget(btn1)

	#function being called by the binding on the button above
	def red(self, obj,**kwargs):
		super(Book, self).__init__(**kwargs)
		#same as above, but the color changes, as well as the text
		btn1 = Button(pos=(650,450),size = (300,300),text = "Green", background_color=(5,1,1,1), font_size=100)
		btn1.bind(on_press=self.green)
		self.add_widget(btn1)

	def green(self, obj,**kwargs):
		super(Book, self).__init__(**kwargs)
		btn1 = Button(pos=(650,450),size = (300,300),text = "Red", background_color=(1,7,1,1), font_size=100)
		btn1.bind(on_press=self.red)
		self.add_widget(btn1)

#clas to return he button set up program
class BookApp(App):
	def build(self):
		return Book()

#run the return program
if __name__ == "__main__":
	myApp = BookApp()
	myApp.run()

	#------------------------------------------------------------------------
#replace the current button code with this for an example of setting the buttons in different locations
#to greact a arcade style GUI
btn1 = Button(pos=(200,450),size = (300,300),text = "Left", background_color=(1,3,5,5), font_size=100)
btn1.bind(on_release=self.end)
self.add_widget(btn1)
btn2 = Button(pos=(1100,450),size = (300,300),text = "Right", background_color=(5,1,1,1), font_size=100)
btn2.bind(on_release=self.end)
self.add_widget(btn2)
btn3 = Button(pos=(650,50),size = (300,300),text = "Down", background_color=(3,1,6,1), font_size=100)
btn3.bind(on_release=self.end)
self.add_widget(btn3)
btn4 = Button(pos=(650,800),size = (300,300),text = "Up", background_color=(1,7,1,1), font_size=100)
btn4.bind(on_release=self.end)
self.add_widget(btn4)

############################################################################

#Box Layout

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

#Buttons class
class MontyHall(BoxLayout):
	def __init__(self,**kwargs):
		super(MontyHall, self).__init__(**kwargs)
		#first button properties: name is door1, color is green, and it is bound to the function door1
		btn1 = Button(text="Door One", background_color = (1,8,1,3))
		btn1.bind(on_press=self.door1)
		self.add_widget(btn1)

		#same but blue and bound to door2
		btn2 = Button(text="Door Two", background_color = (0,0,2,5))
		btn2.bind(on_press=self.door2)
		self.add_widget(btn2)

		#same but orange and bound to door3
		btn3 = Button(text="Door Three", background_color = (7,1,0,1))
		btn3.bind(on_press=self.door3)
		self.add_widget(btn3)

	#functions being called bu clicking on each respective door
	def door1(self, obj):
		#prints this when that door is clicked
		print("Goat")
	def door2(self, obj):
		print("Goat")
	def door3(self, obj):
		print("Car")

#class to return button class
class MHApp(App):
	def build(self):
		return MontyHall()

#run return class
if __name__ == "__main__":
	myApp = MHApp()
	myApp.run()


############################################################################
