from Submarine import Submarine


class Tile:
    def __init__(self, row, column) -> None:
        self.row= row
        self.column= column
        self.has_ship= False
        self.has_hit= False
        self.visited=False
    
    def SetSubmarine(self, submarie):
        self.submarine= submarie
    
    def check_hit(self) -> bool:
        if self.has_ship==True:
            self.has_hit=True
            self.visited=True
            self.submarine.reduceLife()
            return True
        return False

        
        
      

