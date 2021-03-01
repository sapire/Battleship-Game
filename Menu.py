from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.label import Label

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'submarine.jpg'
    

""")

# Declare both screens
class MenuScreen(Screen):
    def __init__(self, controller, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, size=(200,100), size_hint=(None, None))
        self.add_widget(layout)
        self.controller = controller
        
        self.player_name : TextInput = TextInput(size=(200,50), size_hint=(None, None))
        self.start_button : Button = Button(text='Start Game', size=(100,50), size_hint=(None,None))
        layout.add_widget(Widget())
        layout.add_widget(self.player_name)
        layout.add_widget(self.start_button)
        self.bind(center=layout.setter('center'))
        self.start_button.bind(on_press=self.start_game)
        self.player_name.bind(text=self.controller.setter('user_player_name'))

    def start_game(self, instance):
        if not self.player_name.text:
            Popup(title="Can't start game", content=Label(text='Player name not setup'), size_hint=(1,None) ,size=(200,200)).open()
        else:
            self.controller.start_game()

    def on_enter(self):
        self.controller.game_state = 'menu'
