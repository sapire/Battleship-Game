from Tile import Tile
from abc import ABC, abstractmethod
from BattleshipPlayerBoard  import BattleshipPlayerBoard


class IPlayer(ABC):
    """This class is intended to serve as an interface for the HumanPlayer class and the ComputerPlayer class"""

    def __init__(self, name):
        self.player_name = name
        self.player_board = BattleshipPlayerBoard(rowSize=10, colSize=10)

####both maybe depend on GUI? dont do yet.
    @abstractmethod
    def get_move(self):
        pass

    @abstractmethod
    def place_submarines(self):
        pass

####check if player hit and return bool, will use "is_hit"
    def is_player_hit(self, coordinate) -> bool:
        return self.player_board.check_hit(coordinate)
