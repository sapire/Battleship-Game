import BattleshipPlayerBoard

class IPlayer:
    """This class is intended to serve as an interface for the HumanPlayer class and the ComputerPlayer class"""
    def __init__(self, name ):
        self.player_name = name
        self.player_board = BattleshipPlayerBoard()

####both maybe depend on GUI? dont do yet.
    def get_move(self):
        pass

    def place_submarines(self):
        pass
        

####check if player hit and return bool, will use "is_hit"
    def is_player_hit(self) -> bool:
        pass

