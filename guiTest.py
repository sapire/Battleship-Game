
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
        self.controller: BattleshipGameController = controller

        letters = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        for l in letters:
            self.add_widget(Label(text=l))

        self.add_widget(Label(text=''))

        for i in range(1, 11):
            self.add_widget(Label(text=f"{i}"))
            for j in range(1, 11):
                btn = Button(text=" ")
                btn.sq_location = (i - 1, j - 1)
                btn.bind(on_press=self.select)
                self.add_widget(btn)
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

    def select(self, instance: Widget):
        location = instance.sq_location
        res = self.controller.place_submarine(instance.sq_location)

        # for i in self.children:
        #     if self.controller.orientation==">":
