from Submarine import Submarine
from Tile import Tile


class BattleshipPlayerBoard:

    def __init__(self):
        self.grid = []  # The grid (board) of the game.
        self.submarines = []  #

        for i in range(0, 10):
            arr_i = []
            for j in range(0, 10):
                arr_i.append(Tile(i, j))

            self.grid.append(arr_i)

        self.grid[0][0].set_submarine(Submarine("Destroyer", 2))
        self.grid[0][1].set_submarine(Submarine("Destroyer",2))

        self.grid[0][9].set_submarine(Submarine("Submarin", 3))
        self.grid[1][9].set_submarine(Submarine("Submarin", 3))
        self.grid[2][9].set_submarine(Submarine("Submarin", 3))

        

    # ### location=  [ (x1,y1), (x2,y2), ...]

    def check_location(self, locations: list):
        """During the setup stage (when each player places his own ships on his board), this method takes a list of
        coordinates (locations) and checks if it is legal to place a ship there.
        'Locations' is a list of coordinates, in the following format:
        location=  [ (x1,y1), (x2,y2), ...]
        """
        for coord in locations:
            if self.grid[coord[0]][coord[1]].has_ship is True:
                return False  # if there is already a ship on this tile, you can't place another one on top of it.

        if locations[0][0] >= 0 and locations[len(locations) - 1][0] <= 9 and locations[0][1] >= 0 and \
                locations[len(locations) - 1][1] <= 9:
            return True

        return False

    def place_submarine_on_board(self, submarine, locations):
        """This method takes the Submarine object to be placed on the board, and also takes the locations on which
        the submarine will be placed.
        It iterates through the location coordinates and places the Submarine.
        Doesn't return anything."""
        for coord in locations:
            self.grid[coord[0]][coord[1]].set_submarine(submarine)

    def check_hit(self, coordinate):
        print(coordinate)
        return self.grid[coordinate[0]][coordinate[1]].check_hit()


x = BattleshipPlayerBoard(10, 10)
m = Submarine("Shira", 4)
x.place_submarine_on_board(m, [[3, 4], [3, 2]])
