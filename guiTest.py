# import kivy
# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput

# kivy.require('1.0.6') # replace with your current kivy version !

# from kivy.app import App
# from kivy.uix.label import Label

# class Board(GridLayout):
#     def __init__(self):
#         super(Board,self).__init__(**kwargs)
#         self.cols = 10
#         self.rows = 10

#         self.add_widget()


# if __name__ == '__main__':
#     MyApp().run()

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.graphics import *


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        letters = ['','a','b','c','d','e','f','g','h','i','j']
        for l in letters:
            self.add_widget(Label(text=l))

        self.add_widget(Label(text=''))

        for i in range(1,11):
            self.add_widget(Label(text=f"{i}"))
            for j in range(1,11):
                self.add_widget(Button(text=f"Boat{j}"))
            self.add_widget(Label(text=''))
        
        for i in range(1,13):
            self.add_widget(Label(text='_'))

        for l in letters:
            self.add_widget(Label(text=l))

        self.add_widget(Label(text=''))

        for i in range(1,11):
            self.add_widget(Label(text=f"{i}"))
            for j in range(1,11):
                self.add_widget(Button(text=f"Boat{j}"))
            self.add_widget(Label(text=''))
        
        

        # self.rows


class MyApp(App):

    def build(self):
        return LoginScreen(cols=12)


if __name__ == '__main__':
    MyApp().run()