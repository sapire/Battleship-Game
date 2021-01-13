import BattleshipPlayerBoard


class IPlayer:
    """This class is intended to serve as an interface for the HumanPlayer class and the ComputerPlayer class"""

    def __init__(self, name):
        self.player_name = name
        self.player_board = BattleshipPlayerBoard()

    def get_move(self):
        pass

    def place_submarines(self):
        pass

    def is_player_hit(self) -> bool:
        pass
