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

    def get_submarine_name(self, coordinate):
        return self.grid[coordinate[0]][coordinate[1]].get_submarine_name()

    def check_location(self, locations: list):
        """During the setup stage (when each player places his own ships on his board), this method takes a list of
        coordinates (locations) and checks if it is legal to place a ship there.
        'Locations' is a list of coordinates, in the following format:
        location=  [ (x1,y1), (x2,y2), ...]
        """
        try:
            for coord in locations:
                if self.grid[coord[0]][coord[1]].has_ship is True:
                    return False  # if there is already a ship on this tile, you can't place another one on top of it.
        except:
            raise Exception("This ship will be located out of the board")

        return True

    def place_submarine_on_board(self, submarine, locations):
        """This method takes the Submarine object to be placed on the board, and also takes the locations on which
        the submarine will be placed.
        It iterates through the location coordinates and places the Submarine.
        Doesn't return anything."""
        if self.check_location(locations):
            for coord in locations:
                self.grid[coord[0]][coord[1]].set_submarine(submarine)
            return True
        
        return False

    def check_hit(self, coordinate):
        return self.grid[coordinate[0]][coordinate[1]].check_hit()
    
    def get_submarine(self, coordinate):
        tile: Tile = self.grid[coordinate[0]][coordinate[1]]
        return tile.submarine


