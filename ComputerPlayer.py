# ###Note to myself: add stack or something like that to the class property, for the algorithm implementation.
from IPlayer import IPlayer
import random


class ComputerPlayer(IPlayer):
    def __init__(self):
        IPlayer.__init__(self, "Computer")
        self.hit_list = []

    def get_move(self):
        if len(self.hit_list) == 0:  # if there is nothing in the hit_list, choose at random
            rand_col = random.randint(0, 9)
            rand_row = random.randint(0, 9)
            # check if hit, if so add to hit_list

        else:
            coord = self.hit_list[0]

            self.check_location([coord[0] + 1, coord[1]])

    def place_submarines(self):
        pass
