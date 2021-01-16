from IPlayer import IPlayer

class HumanPlayer(IPlayer):
    def __init__(self, name: str):
        IPlayer.__init__(self, name)

    def get_move(self):
        pass

    def place_submarines(self):
        pass