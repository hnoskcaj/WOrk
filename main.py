import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color

class Book(Button):
	def __init__(self,**kwargs):
		super(Book, self).__init__(**kwargs)
		btn1 = Button(pos=(650,450),size = (300,300),text = "Red", background_color=(1,7,1,1), font_size=100)
		btn1.bind(on_press=self.red)
		self.add_widget(btn1)

	def red(self, obj,**kwargs):
		super(Book, self).__init__(**kwargs)
		btn1 = Button(pos=(650,450),size = (300,300),text = "Green", background_color=(5,1,1,1), font_size=100)
		btn1.bind(on_press=self.green)
		self.add_widget(btn1)

	def green(self, obj,**kwargs):
		super(Book, self).__init__(**kwargs)
		btn1 = Button(pos=(650,450),size = (300,300),text = "Red", background_color=(1,7,1,1), font_size=100)
		btn1.bind(on_press=self.red)
		self.add_widget(btn1)

class BookApp(App):
	def build(self):
		return Book()

if __name__ == "__main__":
	myApp = BookApp()
	myApp.run()

