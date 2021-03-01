from IPlayer import IPlayer
import random
from Submarine import *


class ComputerPlayer(IPlayer):
    def __init__(self, controller):
        IPlayer.__init__(self, "Computer", controller)
        self.hit_list = []
        self.nearby_moves = []  # will hold the nearby tiles from the hit_list.
        # for example if in the hit_list we have (2,2), then in the nearby_moves
        # we will have [(1,2), (3, 2), (2, 1), (2, 3)]
        self.moves_made = []  # will hold all the moves (attacks) that were attempted by the computer, whether they
        # were a hit or a miss

    def add_to_hit_list(self, coordinate):
        self.hit_list.append((coordinate[0], coordinate[1]))

    def random_attack(self):
        rand_col = random.randint(0, 9)
        rand_row = random.randint(0, 9)
        # is_hit = self.player_board.check_hit([rand_row, rand_col])  # make move and check if hit
        # if is_hit is True:  # check if hit, if so add to hit_list
        #     self.hit_list.append((rand_row, rand_col))
        return rand_row, rand_col

    def find_nearby_moves(self):
        x, y = self.hit_list.pop()
        if x == 0 or y == 0 or x == 9 or y == 9:  # "walls" of the board
            if x == 0 and y == 0:  # top left corner
                if (x, y + 1) not in self.moves_made:
                    self.nearby_moves.append((x, y + 1))
                if (x+1, y) not in self.moves_made:
                    self.nearby_moves.append((x + 1, y))

            elif x == 9 and y == 9:  # bottom right corner
                if (x - 1, y) not in self.moves_made:
                    self.nearby_moves.append((x - 1, y))
                if (x, y - 1) not in self.moves_made:
                    self.nearby_moves.append((x, y - 1))

            elif x == 0 and y == 9:  #
                if (x + 1, y) not in self.moves_made:
                    self.nearby_moves.append((x + 1, y))
                if (x, y - 1) not in self.moves_made:
                    self.nearby_moves.append((x, y - 1))

            elif x == 9 and y == 0:
                if (x - 1, y) not in self.moves_made:
                    self.nearby_moves.append((x - 1, y))
                if (x, y + 1) not in self.moves_made:
                    self.nearby_moves.append((x, y + 1))

            elif x == 0:
                if (x + 1, y) not in self.moves_made:
                    self.nearby_moves.append((x + 1, y))
                if (x, y + 1) not in self.moves_made:
                    self.nearby_moves.append((x, y + 1))
                if (x, y - 1) not in self.moves_made:
                    self.nearby_moves.append((x, y - 1))

            elif x == 9:
                if (x - 1, y) not in self.moves_made:
                    self.nearby_moves.append((x - 1, y))
                if (x, y - 1) not in self.moves_made:
                    self.nearby_moves.append((x, y - 1))
                if (x, y + 1) not in self.moves_made:
                    self.nearby_moves.append((x, y + 1))

            elif y == 0:
                if (x - 1, y) not in self.moves_made:
                    self.nearby_moves.append((x - 1, y))
                if (x + 1, y) not in self.moves_made:
                    self.nearby_moves.append((x + 1, y))
                if (x, y + 1) not in self.moves_made:
                    self.nearby_moves.append((x, y + 1))

            elif y == 9:
                if (x + 1, y) not in self.moves_made:
                    self.nearby_moves.append((x + 1, y))
                if (x - 1, y) not in self.moves_made:
                    self.nearby_moves.append((x - 1, y))
                if (x, y - 1) not in self.moves_made:
                    self.nearby_moves.append((x, y - 1))

        else:  # not on the walls or corners so we can move anywhere
            if (x - 1, y) not in self.moves_made:
                self.nearby_moves.append((x - 1, y))
            if (x + 1, y) not in self.moves_made:
                self.nearby_moves.append((x + 1, y))
            if (x, y - 1) not in self.moves_made:
                self.nearby_moves.append((x, y - 1))
            if (x, y + 1) not in self.moves_made:
                self.nearby_moves.append((x, y + 1))

    def get_move(self):
        if len(self.nearby_moves) > 0:  # if we have tiles nearby where there was a hit
            x, y = self.nearby_moves.pop()
            # is_hit = self.player_board.check_hit([x, y])
            self.moves_made.append((x, y))  # mark that we made this move so we don't repeat it
            # if is_hit is True:
            #     self.hit_list.append((x, y))
            return x, y

        if len(self.hit_list) == 0:  # if there is nothing in the hit_list, choose at random
            rand_row, rand_col = self.random_attack()
            return rand_row, rand_col

        else:  # there is something in the hit list
            self.find_nearby_moves()
            x, y = self.nearby_moves.pop()
            # is_hit = self.player_board.check_hit([x, y])
            # if is_hit is True:
            #     self.hit_list.append((x, y))
            return x, y

    def get_move(self):
        if len(self.nearby_moves) > 0:  # if we have tiles nearby where there was a hit
            x, y = self.nearby_moves.pop()
            # is_hit = self.player_board.check_hit([x, y])
            self.moves_made.append((x, y))  # mark that we made this move so we don't repeat it
            # if is_hit is True:
            #     self.hit_list.append((x, y))
            return x, y

        if len(self.hit_list) <= 0:  # if there is nothing in the hit_list, choose at random
            rand_row, rand_col = self.random_attack()
            self.moves_made.append((rand_row, rand_col))  # mark that we made this move so we don't repeat it
            return rand_row, rand_col

        if len(self.hit_list) > 0:  # there is something in the hit list
            self.find_nearby_moves()  # we found something in the hit list, so we calculate all the nearby tiles
            # that are on the board and haven't been tried yet
            x, y = self.nearby_moves.pop()
            # is_hit = self.player_board.check_hit([x, y])  # make move
            # if is_hit is True:  # if hit add to hitlist
            #     self.hit_list.append((x, y))
            return x, y

    def place_submarines(self):
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
