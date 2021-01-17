# import BattleshipGameGUI
# import HumanPlayer
# import ComputerPlayer
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

    def start_game(self):
        """We start the game with setup: first the two players place their ships.
        Then, while there is no winner yet, we get the move from the player and then get the move from the computer,
        repeatedly. Once there is a winner, the game is over and the winner's name is announced."""
        self.setup()
        while self.winner is None:
            self.player.get_move()
            self.computer.get_move()
        print("{}wins!", self.winner)

    def update_gui(self):
        pass

    def get_game_state(self):
        """Returns the current state of the board."""
        pass

    def play_human_turn(self, coordinate):
        print(f'human chose {coordinate}')
        value = self.computer.player_board.check_hit(coordinate)
        print(value)
        return value

    def play_computer_turn(self):
        pass

    def setup(self):
        self.player.place_submarines()
        self.computer.place_submarines()
    # ###to-do: 1. function for choose coord by the player


if __name__ == "__main__":
    BattleshipGameController().run()
