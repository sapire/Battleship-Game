# import BattleshipGameGUI
# import HumanPlayer
# import ComputerPlayer
from IPlayer import IPlayer
from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer
from guiTest import Battleship_Screen
from kivy.app import App


class BattleshipGameController(App):
    def build(self):
        return Battleship_Screen(self, cols=12)

    def __init__(self):
        App.__init__(self)
        self.player = HumanPlayer("Moshe")
        self.computer = ComputerPlayer()
        self.is_human_turn = True
        self.winner = None
    
    def get_submarine_name(self, coordinate):
            if self.is_human_turn:
                return self.computer.player_board.get_submarine_name(coordinate)
            else:
                return self.player.player_board.get_submarine_name(coordinate)

        

    def start_game(self):
        """We start the game with setup: first the two players place their ships.
        Then, while there is no winner yet, we get the move from the player and then get the move from the computer,
        repeatedly. Once there is a winner, the game is over and the winner's name is announced."""
        self.setup()
        while self.winner is None:
            self.player.get_move()
            self.computer.get_move()
        print(f"{self.winner}wins!")

    def update_gui(self):
        pass

    def get_game_state(self):
        """Returns the current state of the board. 
        Note: you cant access directly to board, you should go through the player"""
        pass

    def play_human_turn(self, coordinate):
        print(f'Human chose {coordinate}')
        value = self.computer.player_board.check_hit(coordinate)
        print(value)
        return value

    def play_computer_turn(self, coordinate):
        print(f'Computer chose: {coordinate}')
        value = self.player.player_board.check_hit(coordinate)
        print(value)
        return value

    def setup(self):
        """The setup stage takes place before the actual game begins. At this stage each player chooses where to place
        the ships on his own board."""
        self.player.place_submarines()
        self.computer.place_submarines()
    # ###to-do: 1. function for choose coord by the player


if __name__ == "__main__":
    BattleshipGameController().run()
