from IPlayer import IPlayer


class HumanPlayer(IPlayer):
    def __init__(self, name: str, controller):
        IPlayer.__init__(self, name, controller)
        
    def get_move(self):  # delete if unnecessary

        pass

    def place_submarine(self, submarine, location):
        return super().place_submarine(submarine, location)
        # return self.player_board.place_submarine_on_board(submarine, location)


    # def place_submarine(self, submarine, location):
    #     # display message 'Please place all your ships on the board. Ships cannot be on top of each other. All ships
    #     # must be placed before the game can begin'

    #     # show Carrier (5 tiles) to player, the ship should follow the mouse of the player's cursor
    #     # when the user clicks, the submarine should be placed
    #     # move on to place the next submarine until none are left

    #     pass

    def get_score(self):
        score = 1000
        # for every miss, the player loses 100 points
        # for every hit, the player gains 300 points
