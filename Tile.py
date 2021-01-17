from Submarine import Submarine


class Tile:
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column
        self.has_ship = False
        self.has_hit = False
        self.visited = False
        self.submarine = None

    def set_submarine(self, submarine):
        self.submarine = submarine
        self.has_ship = True

    def check_hit(self) -> bool:
        if self.has_ship:
            self.has_hit = True
            self.visited = True
            self.submarine.reduceLife()
            return True
        else:
            self.visited = True
            return False
