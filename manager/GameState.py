from time import sleep

from utilities.Globals import Globals
from utilities.Exceptions import PlayersFileNotFound, PlayersFileIsEmpty
from utilities.FileUtils import FileUtils
from entity.Deck import Deck
from entity.Player import Player
from manager.GameInternalState import GameInternalState


class GameState:

    current_player = 0
    players_page_message = None
    internal_state = GameInternalState.NONE

    def __init__(self, game) -> None:
        self.__game = game
        self.reset()

    def read_players_file(self):

        try:
            self.players = FileUtils.read_players_file(Globals.PLAYERS_FILE_LOCATION)

        except (PlayersFileNotFound, PlayersFileIsEmpty) as e:
            print(e.message)
            sleep(2)
            self.__game.exit()

    def write_state(self):
        FileUtils.write_players_file(Globals.PLAYERS_FILE_LOCATION, self.players)

    def reset(self):
        self.players = []
        self.dealer = Player(name = "Dealer", age = 0, country = "Romania", chips = 0)
        self.current_player = 0
        self.players_page_message = None
        self.deck = Deck()

        self.current_player = 0
        self.internal_state = GameInternalState.NONE
        for player in self.players:
            player.clear_hand()


