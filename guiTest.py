
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
                btn = Button(text=" ")
                btn.sq_location = (i - 1, j - 1)
                btn.bind(on_press=self.select)
                btn.bind(on_hover=self.onHover)
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

    def select(self, instance:Widget):
        location = instance.sq_location
        coordiantes = self.controller.place_submarine(instance.sq_location)

        if coordiantes:
            for i in instance.walk():
                if i.sq_location in coordiantes:
                    instance.background_color = 1,1,1,1
                
                    
    def onHover(self, instance):
        instance.background_color = 61,52,0,68
        
        
                







        # The function place_submarine attempts to position a submarine on the board. if it succeeds it returns true.
        # But even if it does succeeds, it only affects the data in the player board, but the UI is not updated.
        # Now you have to updated the ui if the function returned True.
        # To do so you have to write a loop which iterates over the widgets and you have to find out which of the widgets are those occupied by the boat.
        # A clue: would be to test the value sq_location of each widget against a list of coordinates which hold the ship.
        # PS you may modify the function place_submarine to return the location array of coordinates so it would be easier to compare.



        # for i in self.children:
        #     if self.controller.orientation==">":

        