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
from Menu import MenuScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config



class BattleshipGameController(App, EventDispatcher):
    game_state = StringProperty('menu')
    user_player_name = StringProperty('')
    user_player_score = StringProperty('0')
    computer_player_score = StringProperty('0')

    def __init__(self):
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

        super(BattleshipGameController, self).__init__()
    

    def build(self):
        Config.write()
        sm = ScreenManager(size=(1200,1500))
        sm.add_widget(MenuScreen(name='menu', controller=self, size=(1200,1500)))
        sm.add_widget(Main_screen(name='game', controller=self, size=(1200,1500)))
        self.screen_manager = sm
        return sm
        # return Main_screen(self)

    def on_game_state(self, instance, value):
        if value == 'setup_computer':
            self.computer.place_submarines()
            self.game_state = 'human_turn'
        if value == 'menu':
            self.computer_player_score = 0
            self.user_player_score = 0

        
    def get_submarine_name(self, coordinate):
        if self.is_human_turn:
            return self.computer.player_board.get_submarine_name(coordinate)
        else:
            return self.player.player_board.get_submarine_name(coordinate)

    def start_game(self):
        """We start the game with setup: first the two players place their ships.
        Then, while there is no winner yet, we get the move from the player and then get the move from the computer,
        repeatedly. Once there is a winner, the game is over and the winner's name is announced."""

        self.player = HumanPlayer(self.user_player_name)
        self.computer = ComputerPlayer()
        self.is_human_turn = True
        self.winner = None

        self.submarine_name = None
        self.orientation = '>'
        # self.game_state = StringProperty('setup')
        self.user_submarines_positioned = 0

        self.submarine_name = None
        self.orientation = '>'
        self.user_submarines_positioned = 0

        self.screen_manager.current='game'
        self.game_state = 'setup'

        # self.setup()
        # while self.winner is None:
        #     self.player.get_move()
        #     self.computer.get_move()
        # print(f"{self.winner}wins!")


    def play_human_turn(self, coordinate):
        print(f'Human chose {coordinate}')
        value = self.computer.player_board.check_hit(coordinate)
        if value:
            self.user_player_score = str(int(self.user_player_score) + 1)
        return value

    def play_computer_turn(self):
        coord = self.computer.get_move()
        val = self.player.player_board.check_hit(coord)
        if val:
            self.computer.notify_hit(coord)
            self.computer_player_score = str(int(self.computer_player_score)+ 1)
        return coord, val

    def setup(self):
        """The setup stage takes place before the actual game begins. At this stage each player chooses where to place
        the ships on his own board."""
        self.computer.place_submarines()

    def place_submarine(self, location):
        submarine = Submarine(self.submarine_name)
        locations = []
        for i in range(submarine.life):
            if self.orientation == '>':
                coord = (location[0], location[1] + i)
                locations.append(coord)

            else:
                coord = (location[0] + i, location[1])
                locations.append(coord)

        res = self.player.place_submarine(submarine, locations)
        if res:
            self.user_submarines_positioned = self.user_submarines_positioned + 1
            if self.user_submarines_positioned == 5:
                self.game_state = 'setup_computer'
            return locations
        else:
            raise Exception("Could not locate ship")


if __name__ == "__main__":
    BattleshipGameController().run()
