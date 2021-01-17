####Note to myself: add stack or something like that to the class property, for the algorithm implementation. 
from IPlayer import IPlayer


class ComputerPlayer(IPlayer):
    def __init__(self):
        IPlayer.__init__(self, "Computer")

    def get_move(self):
        pass

    def place_submarines(self):
        pass

    
