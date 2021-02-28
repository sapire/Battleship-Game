# ###Note to myself: add stack or something like that to the class property, for the algorithm implementation.
from IPlayer import IPlayer
import random
from Submarine import *


class ComputerPlayer(IPlayer):
    def __init__(self):
        IPlayer.__init__(self, "Computer")
        self.hit_list = []
        self.nearby_moves = []  # will hold the nearby tiles from the hit_list.
        # for example if in the hit_list we have (2,2), then in the nearby_moves
        # we will have [(1,2), (3, 2), (2, 1), (2, 3)]

    def get_move(self):
        if len(self.nearby_moves) > 0:  # if we have tiles nearby where there was a hit
            x, y = self.nearby_moves.pop()
            is_hit = self.player_board.check_hit([x, y])
            if is_hit is True:
                self.hit_list.append((x, y))
            return x, y

        if len(self.hit_list) == 0:  # if there is nothing in the hit_list, choose at random
            rand_col = random.randint(0, 9)
            rand_row = random.randint(0, 9)
            is_hit = self.player_board.check_hit([rand_row, rand_col])  # make move and check if hit
            if is_hit is True:  # check if hit, if so add to hit_list
                self.hit_list.append((rand_row, rand_col))
            return rand_row, rand_col

        else:  # there is something in the hit list
            x, y = self.hit_list.pop()
            if x == 0 or y == 0 or x == 9 or y == 9:  # "walls" of the board
                if x == 0 and y == 0:  # top left corner
                    self.nearby_moves.append((x, y + 1))
                    self.nearby_moves.append((x + 1, y))
                elif x == 9 and y == 9:  # bottom right corner
                    self.nearby_moves.append((x - 1, y))
                    self.nearby_moves.append((x, y - 1))
                elif x == 0 and y == 9:  #
                    self.nearby_moves.append((x + 1, y))
                    self.nearby_moves.append((x, y - 1))
                elif x == 9 and y == 0:
                    self.nearby_moves.append((x - 1, y))
                    self.nearby_moves.append((x, y + 1))
                elif x == 0:
                    self.nearby_moves.append((x + 1, y))
                    self.nearby_moves.append((x, y + 1))
                    self.nearby_moves.append((x, y - 1))
                elif x == 9:
                    self.nearby_moves.append((x - 1, y))
                    self.nearby_moves.append((x, y - 1))
                    self.nearby_moves.append((x, y + 1))
                elif y == 0:
                    self.nearby_moves.append((x - 1, y))
                    self.nearby_moves.append((x + 1, y))
                    self.nearby_moves.append((x, y + 1))
                elif y == 9:
                    self.nearby_moves.append((x + 1, y))
                    self.nearby_moves.append((x - 1, y))
                    self.nearby_moves.append((x, y - 1))
            else:  # not on the walls or corners so we can move anywhere
                self.nearby_moves.append((x - 1, y))
                self.nearby_moves.append((x + 1, y))
                self.nearby_moves.append((x, y - 1))
                self.nearby_moves.append((x, y + 1))

            x, y = self.nearby_moves.pop()
            is_hit = self.player_board.check_hit([x, y])
            if is_hit is True:
                self.hit_list.append((x, y))
            return x, y

                # rand_move = random.randint(0, 3)  # 0 for left, 1 for right, 2 for up, 3 for down
                # if rand_move == 0:
                #     is_hit = self.player_board.check_hit([x-1, y])
                #     if is_hit:
                #         self.hit_list.append((x-1, y))
                # if rand_move == 1:
                #     is_hit = self.player_board.check_hit([x+1, y])
                #     if is_hit:
                #         self.hit_list.append((x+1, y))
                # if rand_move == 2:
                #     is_hit = self.player_board.check_hit([x, y-1])
                #     if is_hit:
                #         self.hit_list.append((x, y-1))
                # if rand_move == 3:
                #     is_hit = self.player_board.check_hit([x, y+1])
                #     if is_hit:
                #         self.hit_list.append((x, y+1))

            # note to self:
            # 1. if coord from hit list is not in the corners, any adjacent tile will do
            # 2. else, must check the tile exists first
            # 3. Must check when the ship has been destroyed, and delete from hit_list accordingly

            # self.check_location([coord[0] + 1, coord[1]])  # not sure what this was for so commented out

    def place_submarines(self):
        # at the beginning choose a random, valid place on the board for the first ship
        # while there are still ships to place:
        #   choose at random if the ship is vertical or horizontal
        #   then choose at random a place on the board
        #   if the chosen location is invalid, try again

        # Place "Carrier":
        is_carrier_placed = False
        while not is_carrier_placed:
            rand_col = random.randint(0, 1)
            rand_row = random.randint(0, 9)

            my_carrier = Submarine("Carrier")
            location_list = [(rand_col*5, rand_row), (rand_col * 5 + 1, rand_row), (rand_col * 5 + 2, rand_row), (rand_col * 5 + 3, rand_row), (rand_col * 5 + 4, rand_row)]
            is_carrier_placed = self.player_board.place_submarine_on_board(my_carrier, location_list)

        # Place "Battleship":
        is_battleship_placed = False
        while not is_battleship_placed:
            rand_col = random.randint(0, 1)
            rand_row = random.randint(0, 9)

            my_battleship = Submarine("Battleship")
            location_list = [(rand_col * 5, rand_row), (rand_col * 5 + 1, rand_row), (rand_col * 5 + 2, rand_row), (rand_col * 5 + 3, rand_row)]
            is_battleship_placed = self.player_board.place_submarine_on_board(my_battleship, location_list)

        # Place "Cruiser":
        is_cruiser_placed = False
        while not is_cruiser_placed:
            rand_col = random.randint(0, 1)
            rand_row = random.randint(0, 9)

            my_cruiser = Submarine("Cruiser")
            location_list = [(rand_col * 5, rand_row), (rand_col * 5 + 1, rand_row), (rand_col * 5 + 2, rand_row)]
            is_cruiser_placed = self.player_board.place_submarine_on_board(my_cruiser, location_list)

        # Place "Submarine":
        is_submarine_placed = False
        while not is_submarine_placed:
            rand_col = random.randint(0, 1)
            rand_row = random.randint(0, 9)

            my_submarine = Submarine("Submarine")
            location_list = [(rand_col * 5, rand_row), (rand_col * 5 + 1, rand_row), (rand_col * 5 + 2, rand_row)]
            is_submarine_placed = self.player_board.place_submarine_on_board(my_submarine, location_list)

        # Place "Destroyer":
        is_destroyer_placed = False
        while not is_destroyer_placed:
            rand_col = random.randint(0, 1)
            rand_row = random.randint(0, 9)

            my_destroyer = Submarine("Destroyer")
            location_list = [(rand_col * 5, rand_row), (rand_col * 5 + 1, rand_row)]
            is_destroyer_placed = self.player_board.place_submarine_on_board(my_destroyer, location_list)

    def place_submarine(self, submarine, location):
        return super().place_submarine(submarine, location)