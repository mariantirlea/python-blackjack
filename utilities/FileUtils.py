import os.path
from os import path
import re
from utilities.Exceptions import PlayersFileNotFound, PlayersFileIsEmpty
from entity.Player import Player
from utilities.Globals import Globals


class FileUtils:

    @staticmethod
    def read_players_file(filename):

        if not path.exists(filename):
            raise PlayersFileNotFound

        file_handler = open(filename, 'r')
        lines = file_handler.readlines()

        players = []

        for line in lines:
            regex_player_line = "^([^\t]+)\t{1}([^\t]+)\t{1}(\d+)\t{1}([^\t]+)\t{1}(\d+)$"
            result = re.search(regex_player_line, line)

            if result != None and len(result.groups()) == Globals.MAX_FILE_COLUMNS:
                [firstname, lastname, age, country, chips] = result.groups()

                players.append(Player(
                    "{} {}".format(firstname, lastname),
                    int(age),
                    country,
                    int(chips)
                ))

        if not players:
            raise PlayersFileIsEmpty()

        return players
