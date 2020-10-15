import os.path
from os import path
import re
from utilities.Exceptions import PlayersFileNotFound, PlayersFileIsEmpty
from entity.Player import Player
from utilities.Globals import Globals

class FileUtils:

    @staticmethod
    def read_players_file(filename):

        if Globals.DEBUG:
            print('We start reading the players file: ' + filename)

        if not path.exists(filename):
            raise PlayersFileNotFound
            
        file_handler = open(filename, 'r') 
        lines = file_handler.readlines() 
        
        players = []
        for line in lines: 
            regex_player_line = "^([^\t]+)\t{1}([^\t]+)\t{1}(\d+)\t{1}([^\t]+)\t{1}(\d+)$"
            result = re.search(regex_player_line, line)
            
            if result == None:
                if Globals.DEBUG:
                    print('No match')
            else:
                if len(result.groups()) != 5:
                    if Globals.DEBUG:
                        print('No match')
                else:
                    if Globals.DEBUG:
                        print(result.groups())

                    [firstname, lastname, age, country, money] = result.groups()

                    player = Player(
                        "{} {}".format(firstname, lastname),
                        age,
                        country,
                        money
                    )

                    players.append(player)

                    if Globals.DEBUG:    
                        print("Player: " + str(player))
            
        if not players:
            raise PlayersFileIsEmpty()

        if Globals.DEBUG:
            print('Players file was read with {} players'.format(len(players)))

        return players