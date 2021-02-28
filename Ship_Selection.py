
from BattlehipScreen import BattleshipScreen
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Color
from kivy.uix.widget import Widget



class Ship_Selection(BoxLayout):
    def __init__(self,controller, **kwargs):
        super(Ship_Selection, self).__init__(**kwargs)
        self.controller= controller

        self.add_widget(Widget(size_hint=(1, 0.1)))
        arrow= Button(text=">", size= (20, 20), size_hint=(.1, None))
        arrow.bind(on_press=self.orientation)
        self.add_widget(arrow)
        carrier= Button(text="Carrier", size=(100,40),  size_hint=(.5, None))
        carrier.bind(on_press=self.shipSelected)
        self.add_widget(carrier)
        battleship=Button(text="Battleship",size=(80,40), size_hint=(.4, None))
        battleship.bind(on_press=self.shipSelected)
        self.add_widget(battleship)
        cruiser= Button(text="Cruiser",size=(60,40), size_hint=(.3, None))
        cruiser.bind(on_press= self.shipSelected)
        self.add_widget(cruiser)
        submarine= Button(text="Submarine",size=(60,40), size_hint=(.3, None))
        submarine.bind(on_press=self.shipSelected)
        self.add_widget(submarine)
        destroyer= Button(text="Destroyer",size=(40,40),size_hint=(.2, None))
        destroyer.bind(on_press=self.shipSelected)
        self.add_widget(destroyer)
        self.add_widget(Widget())

        self.controller.bind(on_game_state=self.disable_buttons)

    def shipSelected(self,instance):
        self.controller.submarine_name= instance.text
    
    def orientation(self,instance):
        if instance.text == '>':
            instance.text='V'

        else:
            instance.text='>'
            
        self.controller.orientation= instance.text

    def disable_buttons(self, game_state):
        print(instance)








