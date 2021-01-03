import Submarine


class BattleshipPlayerBoard:
    def __init__(self):
        submarine1, submarine2, submarine3, submarine4 = Submarine()
        submarines = (submarine1, submarine2, submarine3, submarine4)  # ## not sure about this implementation, feel
        # free to change
        hits = ()
