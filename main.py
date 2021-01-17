from BattleshipGameGUI import BattleshipGameGUI
from Grid_LayoutApp import GridLayoutApp


if __name__ == '__main__':
    gui = BattleshipGameGUI()
    gui.draw()
    gui.run()
    root = GridLayoutApp()
    root.run()
    print("22")
