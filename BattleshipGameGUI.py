from tkinter import *


class BattleshipGameGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title = "Our beautiful game for methods!!!!"

        self.canvas = Canvas(self.window, width=150, height=150, bg='white')
        self.canvas.pack()

        for i in range(10):
            for j in range(10):
                self.canvas.create_rectangle(i*50, j*50, (i+1)*50, (j+1)*50)

        self.canvas.focus_set()
