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
            if coord[0] == 0 and coord[1] == 0:
                # hit at (1,0) or (0,1)
                pass
            elif coord[0] == 0 and coord[1] != 0:
                # hit at rand at (1, coord[1])
                pass
            elif coord[0] != 0 and coord[1] == 0:
                # hit at rand at (coord[1], 0)
                pass
            elif coord[0] == 9 and coord[1] == 9:
                # hit at rand at (9,8) or (8,9)
                pass
            elif coord[0] == 9 and coord[1] != 9:
                # hit at rand at (
                pass

    def place_submarines(self):
        pass
