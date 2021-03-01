

from Ship_Selection import Ship_Selection
from BattlehipScreen import BattleshipScreen
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

class Main_screen(Screen):
    def __init__(self,controller, **kwargs):
        super(Main_screen, self).__init__(**kwargs)
        self.controller= controller
        self.battleship_screen = BattleshipScreen(controller=controller)
        self.ship_selection= Ship_Selection(controller,size_hint_x=0.3, spacing=10)
        layout = GridLayout(cols=2)

        layout.add_widget(self.battleship_screen)
        layout.add_widget(self.ship_selection)
        self.add_widget(layout)







        
