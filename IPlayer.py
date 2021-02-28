from Tile import Tile
from abc import ABC, abstractmethod
from BattleshipPlayerBoard import BattleshipPlayerBoard


class IPlayer(ABC):
    """This class is intended to serve as an interface for the HumanPlayer class and the ComputerPlayer class"""

    def __init__(self, name):
        """This method assigns the player its name, and creates a new, empty board for him."""
        self.player_name = name
        self.player_board = BattleshipPlayerBoard()
        self.placed_submarines = []

    # ###both maybe depend on GUI? dont do yet.
    @abstractmethod
    def get_move(self):
        pass

    @abstractmethod
    def place_submarine(self, submarine, location):
        if submarine.name in self.placed_submarines:
            raise Exception(f"Cant place {submarine.name} again")
        res = self.player_board.place_submarine_on_board(submarine, location)
        if res:
            self.placed_submarines.append(submarine.name)

        return res

    # ###check if player hit and return bool, will use "is_hit"
    def is_player_hit(self, coordinate) -> bool:
        return self.player_board.check_hit(coordinate)

    def get_submarine_name(self, coordinate):
        return self.player_board.get_submarine_name(coordinate)
