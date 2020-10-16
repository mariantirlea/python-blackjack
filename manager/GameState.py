from time import sleep

from utilities.Globals import Globals
from utilities.Exceptions import PlayersFileNotFound, PlayersFileIsEmpty
from utilities.FileUtils import FileUtils
from entity.Deck import Deck

class GameState:

    current_bet_player = 0
    players_page_message = None

    def __init__(self, game) -> None:
        self.__game = game
        self.reset()

    def read_players_file(self):

        try:
            self.players = FileUtils.read_players_file(Globals.PLAYERS_FILE_LOCATION)

        except (PlayersFileNotFound, PlayersFileIsEmpty) as e:
            print(e.message)
            sleep(2)
            self.__game.__exit()

    def reset(self):
        self.players = []
        self.current_bet_player = 0
        self.players_page_message = None
        self.deck = Deck()