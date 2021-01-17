from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.graphics import *
from kivy.uix.widget import Widget


class Battleship_Screen(GridLayout):

    def __init__(self, controller, **kwargs):
        super(Battleship_Screen, self).__init__(**kwargs)
        self.controller = controller

        letters = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        for l in letters:
            self.add_widget(Label(text=l))

        self.add_widget(Label(text=''))

        for i in range(1, 11):
            self.add_widget(Label(text=f"{i}"))
            for j in range(1, 11):
                self.add_widget(Button(text=f"Boat{j}"))
            self.add_widget(Label(text=''))

        for i in range(1, 13):
            self.add_widget(Label(text='_'))

        for l in letters:
            self.add_widget(Label(text=l))

        self.add_widget(Label(text=''))

        for i in range(1, 11):
            self.add_widget(Label(text=f"{i}"))
            for j in range(1, 11):
                butt = Button(text="pressme")
                butt.bind(on_press=self.press)
                butt.sq_location = (i - 1, j - 1)
                self.add_widget(butt)
            self.add_widget(Label(text=''))

    def press(self, instance: Widget):
        instance.text = f"{instance.sq_location}"
        res = self.controller.play_human_turn(instance.sq_location)
        if not res:
            instance.text="X"
            instance.background_color=[255, 0, 0]

        # elif instance.sq_location==(0,0) or (0,1):
        #     instance.background_color=[104, 61, 235]
            
        

        

            
        
        
        
# class Test(App):

#     def press(self,instance):
#         print("Pressed")
#     def build(self):
#         butt=Button(text="Click")
#         butt.bind(on_press=self.press) #dont use brackets while calling function
#         return butt


#         # self.rows


# class MyApp(App):

#     def build(self):
#         return Battleship_Screen(BattleshipGameController(),  cols=12)


# if __name__ == '__main__':
#     MyApp().run()
