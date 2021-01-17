# import BattleshipGameGUI
# import HumanPlayer
# import ComputerPlayer
from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer
from guiTest import Battleship_Screen
from kivy.app import App


class BattleshipGameController(App):
    def build(self):
        return Battleship_Screen(self,  cols=12)
    
    def __init__(self):
        App.__init__(self)
        self.player = HumanPlayer("Moshe")
        self.computer = ComputerPlayer()
        self.is_human_turn = True

    def start_game(self):
        pass

    def update_gui(self):
        pass

    def get_game_state(self):
        pass

    def play_human_turn(self, coordinate):
        print(f'human chose {coordinate}')
        
        pass

    def play_computer_turn(self):
        pass
    

    ####to-do: 1. function for choose coord by the player


if __name__ == "__main__":
    BattleshipGameController().run()