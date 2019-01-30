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
