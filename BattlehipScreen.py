
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager  import Screen
from kivy.properties import StringProperty

from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.core.window import Window


class BattleshipScreenInfo(BoxLayout):
    def __init__(self, controller):
        super(BattleshipScreenInfo, self).__init__(orientation='horizontal', spacing=20, size_hint=(1, None))
        self.controller = controller
        self.playername : Label = Label(text='')
        self.playerscore = Label(text='0')
        self.computername : Label = Label(text='Computer')
        self.computerscore = Label(text='0')

        controller.bind(user_player_name=self.playername.setter('text'))
        controller.bind(user_player_score=self.playerscore.setter('text'))
        controller.bind(computer_player_score=self.computerscore.setter('text'))

        self.add_widget(self.playername)
        self.add_widget(self.playerscore)
        self.add_widget(self.computername)
        self.add_widget(self.computerscore)

        controller.bind(user_player_score=self.check_score_victory_user)
        controller.bind(computer_player_score=self.check_score_victory_computer)

        controller.bind(game_state=self.show_active_turn)

    def show_active_turn(self, instance, value):
        if value == 'human_turn':
            self.playername.outline_color = 1,1,1,1
            self.computername.outline_color = 0,0,0,0
        elif value == 'computer_turn':
            self.computername.outline_color = 1,1,1,1
            self.playername.outline_color = 0,0,0,0
        else:
            self.playername.outline_color = 0,0,0,0
            self.playername.outline_color = 0,0,0,0



        
        

    def check_score_victory_user(self, instance, value):
        if int(value) < 17:
            return
        
        Popup(title='Victory !!!', content=Label(text='User Won !!!!'), size_hint=(1,None) ,size=(200,200)).open()
        self.controller.screen_manager.current = 'menu'
        
    def check_score_victory_computer(self, instance, value):
        if int(value) < 17:
            return
        
        Popup(title='You Lost !!!', content=Label(text='Coputer Won !!!!'), size_hint=(1,None) ,size=(200,200)).open()
        
        self.controller.screen_manager.current = 'menu'


class BattleshipScreen(BoxLayout):

    def __init__(self, controller, **kwargs):
        super(BattleshipScreen, self).__init__(**kwargs, orientation='vertical')
        
        self.controller = controller
        self.controller.bind(game_state=self.game_state_listen)
        
        self.topGrid : GridLayout = GridLayout(cols=12)
        self.bottomGrid : GridLayout = GridLayout(cols=12)
        self.add_widget(BattleshipScreenInfo(controller=self.controller))
        self.add_widget(self.topGrid)
        self.add_widget(self.bottomGrid)
        self.played_cooridinates = []

        letters = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        for l in letters:
            self.topGrid.add_widget(Label(text=l))

        self.topGrid.add_widget(Label(text=''))

        for i in range(1, 11):
            self.topGrid.add_widget(Label(text=f"{i}"))
            for j in range(1, 11):
                btn = Button(text=" ")
                btn.sq_location = (i - 1, j - 1)
                btn.bind(on_press=self.select)
                self.topGrid.add_widget(btn)
            self.topGrid.add_widget(Label(text=''))

        # for i in range(1, 13):
        #     self.add_widget(Label(text='______'))

        for l in letters:
            self.bottomGrid.add_widget(Label(text=l))

        self.bottomGrid.add_widget(Label(text=''))

        for i in range(1, 11):
            self.bottomGrid.add_widget(Label(text=f"{i}"))
            for j in range(1, 11):
                butt = Button(text=" ")
                butt.bind(on_press=self.press)
                butt.sq_location = (i - 1, j - 1)
                self.bottomGrid.add_widget(butt)
            self.bottomGrid.add_widget(Label(text=''))

    def set_initial_state(self):
        for widget in self.topGrid.walk():
            if hasattr(widget, 'sq_location'):
                widget.background_color = 1,1,1,1
                widget.text = ''
        
        for widget in self.bottomGrid.walk():
            if hasattr(widget, 'sq_location'):
                widget.background_color = 1,1,1,1
                widget.text = ''

    def press(self, instance: Widget):
        if self.controller.game_state == 'setup':
            Popup(title="Invalid move !", content=Label(text="You still need to position your submarines !"), size_hint=(1,None) ,size=(200,200)).open()
            return
        if instance.sq_location in self.played_cooridinates:
            Popup(title="Invalid move !", content=Label(text="You can't play the same square again !"), size_hint=(1,None) ,size=(200,200)).open()
            return
        self.played_cooridinates.append(instance.sq_location)
        res = self.controller.play_human_turn(instance.sq_location)
        if not res:
            instance.text = "X"
            instance.background_color = 1, 0, 0, 1
        else:
            instance.text = ' '
            name = self.controller.get_submarine_name(instance.sq_location)
            if name == "Destroyer":
                instance.background_color = 1, 0, 1, 1  # dark pink
            if name == "Submarine":
                instance.background_color = 0, 1, 1, 1  # dark turquoise (blue)
            if name == "Cruiser":
                instance.background_color = 0, 0, 1, 10  # dark blue
            if name == "Battleship":
                instance.background_color = 2, 0, 1, 2  # pink
            if name == "Carrier":
                instance.background_color = 0, 1, 0, 1  # dark green
        self.controller.game_state='computer_turn'

    def select(self, instance:Button):
        try:
            coordiantes = self.controller.place_submarine(instance.sq_location)
            print(coordiantes)
            if coordiantes:
                for i in self.topGrid.walk(restrict=True):
                    if hasattr(i, 'sq_location') and i.sq_location in coordiantes:
                        i.background_color = 2, 0, 1, 2
                        # 1,0,0,1

        except Exception as err:
            Popup(title='Error positioning submarine', content=Label(text=f"{err}"), size_hint=(1,None) ,size=(200,200)).open()

    def game_state_listen(self, instance, game_state):
        if game_state=='computer_turn':
            coord, res=self.controller.play_computer_turn()
            if res==False:
                for widg in self.topGrid.walk(restrict=True):
                    if hasattr(widg, 'sq_location') and widg.sq_location == coord:
                        widg.text='X'
                        widg.background_color=195, 98, 96, 1
            else:
                for widg in self.topGrid.walk(restrict=True):
                    if hasattr(widg, 'sq_location') and widg.sq_location == coord:
                        widg.text=''
                        widg.background_color= 0, 0, 1, 10
            self.controller.game_state='human_turn'
        elif game_state == 'setup':
            self.set_initial_state()
            self.played_cooridinates = []
            

                   
                        
                

     

        


