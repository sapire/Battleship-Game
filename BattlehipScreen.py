
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from kivy.graphics import Color
from kivy.uix.widget import Widget


class BattleshipScreen(BoxLayout):

    def __init__(self, controller, **kwargs):
        super(BattleshipScreen, self).__init__(orientation='vertical')
        self.controller = controller
        self.topGrid : GridLayout = GridLayout(cols=12)
        self.bottomGrid : GridLayout = GridLayout(cols=12)
        self.add_widget(self.topGrid)
        self.add_widget(self.bottomGrid)

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

    def select(self, instance:Button):
        # try:
            coordiantes = self.controller.place_submarine(instance.sq_location)
            print(coordiantes)
            if coordiantes:
                for i in self.topGrid.walk(restrict=True):
                    if hasattr(i, 'sq_location') and i.sq_location in coordiantes:
                        i.background_color = 1,0,0,1

        # except Exception as err:
        #     Popup(title='Error positioning submarine', content=Label(text=f"{err}"), size_hint=(1,None) ,size=(200,200)).open()
            
        

        

        
