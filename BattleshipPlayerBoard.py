from Submarine import Submarine
from Tile import Tile


class BattleshipPlayerBoard:

    def __init__(self, rowSize, colSize):

        # self.rowSize=10
        # self.colSize=10
        self.grid = []
        self.submarines = []

        for i in range(0, 10):
            arr_i = []
            for j in range(0, 10):
                arr_i.append(Tile(i, j))

            self.grid.append(arr_i)

    # ### location=  [ (x1,y1), (x2,y2), ...]

    def check_location(self, submarin: Submarine, locations: list):

        for coord in locations:
            if self.grid[coord[0]][coord[1]].has_ship == True:
                return False

        if locations[0][0] >= 0 and locations[len(locations)-1][0] <= 9 and locations[0][1] >= 0 and locations[len(locations)-1][1] <= 9:
            return True
            
        return False
    
    def place_submarine_on_board(self, submarin, locations):
        
        for coord in locations:
            self.grid[coord[0]][coord[1]].set_submarine(submarin)
    
    def check_hit(self, coordinate):
        print(coordinate)
        return self.grid[coordinate[0]][coordinate[1]].check_hit()

