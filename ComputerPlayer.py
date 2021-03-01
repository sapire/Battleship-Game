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

    def add_to_hit_list(self, coordinate):
        self.hit_list.append((coordinate[0], coordinate[1]))

    def get_move(self):
        if len(self.nearby_moves) > 0:  # if we have tiles nearby where there was a hit
            x, y = self.nearby_moves.pop()
            return x, y

        if len(self.hit_list) == 0:  # if there is nothing in the hit_list, choose at random
            rand_col = random.randint(0, 9)
            rand_row = random.randint(0, 9)
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
            return x, y

    def place_submarines(self):
        # at the beginning choose a random, valid place on the board for the first ship
        # while there are still ships to place:
        #   choose at random if the ship is vertical or horizontal
        #   then choose at random a place on the board
        #   if the chosen location is invalid, try again

        # Place "Carrier":
        is_carrier_placed = False
        while not is_carrier_placed:
            horiz_or_vert = random.randint(0, 1)
            if horiz_or_vert == 0:
                rand_col = random.randint(0, 1)
                rand_row = random.randint(0, 9)
                location_list = [(rand_col * 5, rand_row), (rand_col * 5 + 1, rand_row), (rand_col * 5 + 2, rand_row),
                                 (rand_col * 5 + 3, rand_row), (rand_col * 5 + 4, rand_row)]
            if horiz_or_vert == 1:
                rand_col = random.randint(0, 9)
                rand_row = random.randint(0, 1)
                location_list = [(rand_col, rand_row * 5), (rand_col, rand_row * 5 + 1), (rand_col, rand_row * 5 + 2),
                                 (rand_col, rand_row * 5 + 3), (rand_col, rand_row * 5 + 4)]

            my_carrier = Submarine("Carrier")
            is_carrier_placed = self.player_board.place_submarine_on_board(my_carrier, location_list)

        # Place "Battleship":
        is_battleship_placed = False
        while not is_battleship_placed:
            horiz_or_vert = random.randint(0, 1)
            if horiz_or_vert == 0:
                rand_col = random.randint(0, 1)
                rand_row = random.randint(0, 9)
                location_list = [(rand_col * 5, rand_row), (rand_col * 5 + 1, rand_row), (rand_col * 5 + 2, rand_row),
                                 (rand_col * 5 + 3, rand_row)]
            if horiz_or_vert == 1:
                rand_col = random.randint(0, 9)
                rand_row = random.randint(0, 1)
                location_list = [(rand_col, rand_row * 5), (rand_col, rand_row * 5 + 1), (rand_col, rand_row * 5 + 2),
                                 (rand_col, rand_row * 5 + 3)]

            my_battleship = Submarine("Battleship")
            is_battleship_placed = self.player_board.place_submarine_on_board(my_battleship, location_list)

        # Place "Cruiser":
        is_cruiser_placed = False
        while not is_cruiser_placed:
            horiz_or_vert = random.randint(0, 1)
            if horiz_or_vert == 0:
                rand_col = random.randint(0, 1)
                rand_row = random.randint(0, 9)
                location_list = [(rand_col * 5, rand_row), (rand_col * 5 + 1, rand_row), (rand_col * 5 + 2, rand_row)]
            if horiz_or_vert == 1:
                rand_col = random.randint(0, 9)
                rand_row = random.randint(0, 1)
                location_list = [(rand_col, rand_row * 5), (rand_col, rand_row * 5 + 1), (rand_col, rand_row * 5 + 2)]

            my_cruiser = Submarine("Cruiser")
            is_cruiser_placed = self.player_board.place_submarine_on_board(my_cruiser, location_list)

        # Place "Submarine":
        is_submarine_placed = False
        while not is_submarine_placed:
            horiz_or_vert = random.randint(0, 1)
            if horiz_or_vert == 0:
                rand_col = random.randint(0, 1)
                rand_row = random.randint(0, 9)
                location_list = [(rand_col * 5, rand_row), (rand_col * 5 + 1, rand_row), (rand_col * 5 + 2, rand_row)]
            if horiz_or_vert == 1:
                rand_col = random.randint(0, 9)
                rand_row = random.randint(0, 1)
                location_list = [(rand_col, rand_row * 5), (rand_col, rand_row * 5 + 1), (rand_col, rand_row * 5 + 2)]

            my_submarine = Submarine("Submarine")
            is_submarine_placed = self.player_board.place_submarine_on_board(my_submarine, location_list)

        # Place "Destroyer":
        is_destroyer_placed = False
        while not is_destroyer_placed:
            horiz_or_vert = random.randint(0, 1)
            if horiz_or_vert == 0:
                rand_col = random.randint(0, 1)
                rand_row = random.randint(0, 9)
                location_list = [(rand_col * 5, rand_row), (rand_col * 5 + 1, rand_row)]
            if horiz_or_vert == 1:
                rand_col = random.randint(0, 9)
                rand_row = random.randint(0, 1)
                location_list = [(rand_col, rand_row * 5), (rand_col, rand_row * 5 + 1)]

            my_destroyer = Submarine("Destroyer")
            is_destroyer_placed = self.player_board.place_submarine_on_board(my_destroyer, location_list)

    def place_submarine(self, submarine, location):
        return super().place_submarine(submarine, location)

    def notify_hit(self, location):
        self.hit_list.append(location)
