from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget



class Ship_Selection(BoxLayout):
    def __init__(self,controller, **kwargs):
        super(Ship_Selection, self).__init__(**kwargs)
        self.controller= controller

        self.add_widget(Widget(size_hint=(1, 0.1)))
        self.arrow= Button(text=">", size= (20, 20), size_hint=(None, None))
        self.arrow.bind(on_press=self.orientation)
        self.add_widget(self.arrow)
        self.carrier= Button(text="Carrier", size=(140,40),  size_hint=(None, None))
        self.carrier.bind(on_press=self.shipSelected)
        self.add_widget(self.carrier)
        self.battleship=Button(text="Battleship",size=(110,40), size_hint=(None, None))
        self.battleship.bind(on_press=self.shipSelected)
        self.add_widget(self.battleship)
        self.cruiser= Button(text="Cruiser",size=(90,40), size_hint=(None, None))
        self.cruiser.bind(on_press= self.shipSelected)
        self.add_widget(self.cruiser)
        self.submarine= Button(text="Submarine",size=(90,40), size_hint=(None, None))
        self.submarine.bind(on_press=self.shipSelected)
        self.add_widget(self.submarine)
        self.destroyer= Button(text="Destroyer",size=(70,40),size_hint=(None, None))
        self.destroyer.bind(on_press=self.shipSelected)
        self.add_widget(self.destroyer)
        self.add_widget(Widget())
        self.add_widget(Widget())
        self.leave_game = Button(text="Leave game", size=(100,40), size_hint=(None,None))
        self.leave_game.bind(on_press=self.exit_game)
        self.add_widget(self.leave_game)


        self.controller.bind(game_state=self.disable_buttons)

    def shipSelected(self,instance):
        self.controller.submarine_name= instance.text
    
    def orientation(self,instance):
        if instance.text == '>':
            instance.text='V'

        else:
            instance.text='>'
            
        self.controller.orientation= instance.text
 
    def disable_buttons(self, instance, game_state):
        if game_state == 'setup':
            self.submarine.disabled = False
            self.arrow.disabled = False
            self.carrier.disabled = False
            self.battleship.disabled = False
            self.destroyer.disabled = False
            self.cruiser.disabled = False
        else:
            self.submarine.disabled = True
            self.arrow.disabled = True
            self.carrier.disabled = True
            self.battleship.disabled = True
            self.destroyer.disabled = True
            self.cruiser.disabled = True
            

    def exit_game(self, instance):
        self.controller.screen_manager.current = 'menu'






