from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.graphics import Color
from kivy.uix.widget import Widget


class BattleshipScreen(GridLayout):

    def __init__(self, controller, **kwargs):
        super(BattleshipScreen, self).__init__(**kwargs)
        self.controller = controller

        letters = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        for l in letters:
            self.add_widget(Label(text=l))

        self.add_widget(Label(text=''))

        for i in range(1, 11):
            self.add_widget(Label(text=f"{i}"))
            for j in range(1, 11):
                if (i, j) in [(1, 1), (2, 1), (3, 1)] or (i, j) in [(5, 5,), (5, 6), (5, 7), (5, 8)] or (i, j) in [
                    (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)] or (i, j) in [(2, 8), (2, 9)] or (i, j) in [(6, 1), (7, 1),
                                                                                                        (8, 1), (9, 1)]:
                    self.add_widget(Button(text=" ", background_color=(255, 255, 255)))
                else:
                    self.add_widget(Button(text=" "))
            self.add_widget(Label(text=''))

        for i in range(1, 13):
            self.add_widget(Label(text='______'))

        for l in letters:
            self.add_widget(Label(text=l))

        self.add_widget(Label(text=''))

        for i in range(1, 11):
            self.add_widget(Label(text=f"{i}"))
            for j in range(1, 11):
                butt = Button(text=" ")
                butt.bind(on_press=self.press)
                butt.sq_location = (i - 1, j - 1)
                self.add_widget(butt)
            self.add_widget(Label(text=''))

    def press(self, instance: Widget):
        instance.text = f"{instance.sq_location}"
        res = self.controller.play_human_turn(instance.sq_location)
        if not res:
            instance.text = "X"
            instance.background_color = 1, 0, 0, 1
        else:
            instance.text = ' '
            name = self.controller.get_submarine_name(instance.sq_location)
            if name == "Destroyer":
                instance.background_color = 1, 0, 1, 1
            if name == "Submarine":
                instance.background_color = 0, 1, 1, 1
            if name == "Cruiser":
                instance.background_color = 1, 0, 0, 0
            if name == "Battleship":
                instance.background_color = 0, 50, 0, 1
            if name == "Carrier":
                instance.background_color = 61, 52, 0, 68

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
#         return BattleshipScreen(BattleshipGameController(),  cols=12)


# if __name__ == '__main__':
#     MyApp().run()
