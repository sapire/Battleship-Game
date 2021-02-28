from configparser import Error


class Submarine:
    def __init__(self, name):
        if name == "Carrier":
            self.name = name
            self.life = 5

        elif name == "Battleship":
            self.name = name
            self.life = 4

        elif name == "Cruiser":
            self.name = name
            self.life = 3

        elif name == "Submarine":
            self.name = name
            self.life = 3

        elif name == "Destroyer":
            self.name = name
            self.life = 2

        else:
            raise Error("Error while trying to create submarine. Submarine name can only be one of the following:"
                  "Carrier, Battleship, Cruiser, Submarine, Destroyer")

        # self.name = name
        # self.life = life
        self.locations = None
        # ###location=(x1,y2)

    def reduce_life(self):
        """This method reduces the number of lives of the ship by one.
        Receives and returns nothing."""
        self.life -= 1

    def check_sunk(self):
        """This method tells us if a submarine has sunk.
        If all of the coordinates of the ship were hit, it has zero life, which means it has sunk."""
        if self.life == 0:
            return True
        return False

    def get_submarine_name(self):
        return self.name
