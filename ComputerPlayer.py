# ###Note to myself: add stack or something like that to the class property, for the algorithm implementation.
from IPlayer import IPlayer
import random
from Submarine import *


class ComputerPlayer(IPlayer):
    def __init__(self):
        IPlayer.__init__(self, "Computer")
        self.hit_list = []

    def get_move(self):
        if len(self.hit_list) == 0:  # if there is nothing in the hit_list, choose at random
            rand_col = random.randint(0, 9)
            rand_row = random.randint(0, 9)
            is_hit = self.player_board.check_hit([rand_row, rand_col])
            if is_hit is True:
                self.hit_list.append((rand_row, rand_col))
            # check if hit, if so add to hit_list

        else:  # there is something in the hit list
            x, y = self.hit_list[0]
            corners = [(0, 0), (0, 9), (9, 0), (9, 9)]
            if x == 0 or y == 0 or x == 9 or y == 9:  # "walls" of the board
                pass

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
            # check if the spot is available
            if self.player_board[rand_col * 5][rand_row] is None and self.player_board[rand_col * 5 + 1][
                rand_row] is None and self.player_board[rand_col * 5 + 2][rand_row] is None and \
                    self.player_board[rand_col * 5 + 3][rand_row] is None and self.player_board[rand_col * 5 + 4][
                rand_row] is None:
                my_carrier = Submarine("Carrier")
                location_list = [(rand_col * 5, rand_row), (rand_col * 5 + 1, rand_row), (rand_col * 5 + 2, rand_row),
                                 (rand_col * 5 + 3, rand_row), (rand_col * 5 + 4, rand_row)]
                self.player_board.place_submarine_on_board(my_carrier, location_list)
                is_carrier_placed = True

        # Place "Battleship":
        is_battleship_placed = False
        while not is_battleship_placed:
            rand_col = random.randint(0, 1)
            rand_row = random.randint(0, 9)
            # check if the spot is available
            if self.player_board[rand_col * 5][rand_row] is None and self.player_board[rand_col * 5 + 1][
                rand_row] is None and self.player_board[rand_col * 5 + 2][rand_row] is None and \
                    self.player_board[rand_col * 5 + 3][rand_row] is None:
                my_battleship = Submarine("Battleship")
                location_list = [(rand_col * 5, rand_row), (rand_col * 5 + 1, rand_row), (rand_col * 5 + 2, rand_row),
                                 (rand_col * 5 + 3, rand_row)]
                self.player_board.place_submarine_on_board(my_battleship, location_list)
                is_battleship_placed = True

        # Place "Cruiser":
        is_cruiser_placed = False
        while not is_cruiser_placed:
            rand_col = random.randint(0, 1)
            rand_row = random.randint(0, 9)
            # check if the spot is available
            if self.player_board[rand_col * 5][rand_row] is None and self.player_board[rand_col * 5 + 1][
                rand_row] is None and self.player_board[rand_col * 5 + 2][rand_row] is None:
                my_cruiser = Submarine("Cruiser")
                location_list = [(rand_col * 5, rand_row), (rand_col * 5 + 1, rand_row), (rand_col * 5 + 2, rand_row)]
                self.player_board.place_submarine_on_board(my_cruiser, location_list)
                is_cruiser_placed = True

        # Place "Submarine":
        is_submarine_placed = False
        while not is_submarine_placed:
            rand_col = random.randint(0, 1)
            rand_row = random.randint(0, 9)
            # check if the spot is available
            if self.player_board[rand_col * 5][rand_row] is None and self.player_board[rand_col * 5 + 1][
                rand_row] is None and self.player_board[rand_col * 5 + 2][rand_row] is None:
                my_submarine = Submarine("Submarine")
                location_list = [(rand_col * 5, rand_row), (rand_col * 5 + 1, rand_row), (rand_col * 5 + 2, rand_row)]
                self.player_board.place_submarine_on_board(my_submarine, location_list)
                is_submarine_placed = True

        # Place "Destroyer":
        is_destroyer_placed = False
        while not is_destroyer_placed:
            rand_col = random.randint(0, 1)
            rand_row = random.randint(0, 9)
            # check if the spot is available
            if self.player_board[rand_col * 5][rand_row] is None and self.player_board[rand_col * 5 + 1][
                rand_row] is None:
                my_destroyer = Submarine("Destroyer")
                location_list = [(rand_col * 5, rand_row), (rand_col * 5 + 1, rand_row)]
                self.player_board.place_submarine_on_board(my_destroyer, location_list)
                is_destroyer_placed = True
