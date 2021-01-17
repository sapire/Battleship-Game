from BattleshipGameGUI import BattleshipGameGUI
from Grid_LayoutApp import GridLayoutApp


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gui = BattleshipGameGUI()
    gui.draw()
    gui.run()
    root = GridLayoutApp()
    root.run()
    print("22")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
