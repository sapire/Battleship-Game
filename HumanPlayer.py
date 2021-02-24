from IPlayer import IPlayer


class HumanPlayer(IPlayer):
    def __init__(self, name: str):
        IPlayer.__init__(self, name)

    def get_move(self):  # delete if unnecessary

        pass

    def place_submarines(self):
        # display message 'Please place all your ships on the board. Ships cannot be on top of each other. All ships
        # must be placed before the game can begin'

        # show Carrier (5 tiles) to player, the ship should follow the mouse of the player's cursor
        # when the user clicks, the submarine should be placed
        # move on to place the next submarine until none are left
        pass
