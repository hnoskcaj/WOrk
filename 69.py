import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MontyHall(BoxLayout):
	def __init__(self,**kwargs):
		super(MontyHall, self).__init__(**kwargs)
		btn1 = Button(text="Door One", background_color = (1,8,1,3))
		btn1.bind(on_press=self.door1)
		self.add_widget(btn1)

		btn2 = Button(text="Door Two", background_color = (0,0,2,5))
		btn2.bind(on_press=self.door2)
		self.add_widget(btn2)

		btn3 = Button(text="Door Three", background_color = (7,1,0,1))
		btn3.bind(on_press=self.door3)
		self.add_widget(btn3)

	def door1(self, obj):
		print("Goat")
	def door2(self, obj):
		print("Goat")
	def door3(self, obj):
		print("Car")

class MHApp(App):
	def build(self):
		return MontyHall()


if __name__ == "__main__":
	myApp = MHApp()
	myApp.run()