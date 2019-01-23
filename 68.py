import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout


class Book(App):
	def build(self):
		self.button = Button(text = "hi", background_color = (3,3,1,1), font_size = 100)
		# self.button.bind(on_release=start)
		return Button

# def start():
# 	print("go!")

if __name__ == "__main__":
	Book().run()


# class Book(App):
# 	def build(self):
# 		f = FloatLayout()
# 		s = Scatter()
# 		l = Label(text = "Hello world", font_size = 150)

# 		f.add_widget(s)
# 		s.add_widget(l)
# 		return f

# Book().run()