# import BattleshipGameGUI
# import HumanPlayer
# import ComputerPlayer
from logging import LoggerAdapter
from Submarine import Submarine
from MainScreen import Main_screen
from IPlayer import IPlayer
from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer
from BattlehipScreen import BattleshipScreen
from kivy.app import App
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.event import EventDispatcher

class BattleshipGameController(App, EventDispatcher):
    game_state = StringProperty('setup')
    
    def build(self):
        return Main_screen(self)

    def on_game_state(self, instance, value):
        if value == 'setup_computer':
            self.computer.place_submarines()
            self.game_state = 'human_turn'
            
       

    def __init__(self):
        super(BattleshipGameController, self).__init__()
        self.player = HumanPlayer("Moshe")
        self.computer = ComputerPlayer()
        self.is_human_turn = True
        self.winner = None
        self.submarine_name=None
        self.orientation='>'
        self.user_submarines_positioned = 0
     

    def get_submarine_name(self, coordinate):
        if self.is_human_turn:
            return self.computer.player_board.get_submarine_name(coordinate)
        else:
            return self.player.player_board.get_submarine_name(coordinate)

    def start_game(self):
        """We start the game with setup: first the two players place their ships.
        Then, while there is no winner yet, we get the move from the player and then get the move from the computer,
        repeatedly. Once there is a winner, the game is over and the winner's name is announced."""
        self.setup()
        while self.winner is None:
            self.player.get_move()
            self.computer.get_move()
        print(f"{self.winner}wins!")

    def update_gui(self):  # remove if unnecessary
        pass

    def get_game_state(self):  # remove if unnecessary
        """Returns the current state of the board. 
        Note: you cant access directly to board, you should go through the player"""
        pass

    def play_human_turn(self, coordinate):
        print(f'Human chose {coordinate}')
        value = self.computer.player_board.check_hit(coordinate)
        return value

    def play_computer_turn(self, coordinate):
        print(f'Computer chose: {coordinate}')
        value = self.player.player_board.check_hit(coordinate)
        print(value)
        return value

    def setup(self):
        """The setup stage takes place before the actual game begins. At this stage each player chooses where to place
        the ships on his own board."""
        self.computer.place_submarines()
    # ###to-do: 1. function for choose coord by the player

    def place_submarine(self, location):
        submarine = Submarine(self.submarine_name)
        locations= []
        for i in range(submarine.life):
            if self.orientation=='>':
                coord=(location[0],location[1]+i)
                locations.append(coord)

            else:
                coord=(location[0]+i, location[1])
                locations.append(coord)
                
                        

        res = self.player.place_submarine(submarine, locations)
        if res:
            self.user_submarines_positioned = self.user_submarines_positioned + 1
            if (self.user_submarines_positioned == 5):
                self.game_state = 'setup_computer'
            return locations
        else:
            raise Exception("Could not locate ship")


        
if __name__ == "__main__":
    BattleshipGameController().run()
