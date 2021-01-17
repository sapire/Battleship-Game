import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
import kivy.uix.behaviors


class GridLayoutApp(GridLayout):
    def __init__(self, **kwargs):
        super(GridLayoutApp, self).__init__(**kwargs)
        self.cols = 20

        self.my_board = GridLayout()
        self.my_board.cols = 10
        self.my_board_buttons_list = []
        for i in range(0, 10):
            col = []
            for ii in range(0, 10):
                col.append(Button(text=" ", background_color=(68, 0, 102, 0.8)))
                col[ii].on_press()
                self.my_board.add_widget(col[ii])
            self.my_board_buttons_list.append(col)

        self.add_widget(self.my_board)

        self.computer_board = GridLayout()
        self.computer_board.cols = 10

        for i in range(0, 10):
            for ii in range(0, 10):
                self.computer_board.add_widget(Button(text=" ", background_color=(98, 23, 1, 1)))

        self.add_widget(self.computer_board)

    def callback(self, i, ii):
        print("pressed ", i, ii)

    def build(self):

        layout = GridLayout(cols=20)
        # for i in range(0, 2):
        #     layout.add_widget(self.inside)
        # for i in range(0, 10):
        #     for ii in range(0, 20):
        #         layout.add_widget(Button(text=' '))

        return layout


class MyApp(App):
    def build(self):
        self.title = "Battleship Game"
        return GridLayoutApp()


root = MyApp()
root.run()
