class Submarine:
    def __init__(self, name, life):
        self.name = name
        self.life = life
        self.locations = None
        # ###location=(x1,y2)

    def reduce_life(self):
        self.life += -1

    # check if submarine sunk=> zero life
    def check_sunk(self):
        if self.life == 0:
            return True
        return False

    def create_submarine(name: str):

        if name == "Carrier":
            submarine = Submarine(name, 5)
            return submarine
        if name == "Battleship":
            submarine = Submarine(name, 4)
            return submarine
        if name == "Cruiser":
            submarine = Submarine(name, 3)
            return submarine
        if name == "Submarin":
            submarine = Submarine(name, 3)
            return submarine
        if name == "Destroyer":
            submarine = Submarine(name, 2)
            return submarine
