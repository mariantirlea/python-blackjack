import os.path
from os import path
from utilities.Exceptions import PlayersFileNotFound, PlayersFileIsEmpty
from entity.Player import Player

class FileUtils:

    @staticmethod
    def read_players_file(filename):
        print('We start reading the players file: ' + filename)

        if not path.exists(filename):
            raise PlayersFileNotFound
            
        file_handler = open(filename, 'r') 
        lines = file_handler.readlines() 
        
        players = []
        for line in lines: 
            lines_part = line.strip().split("\t")

            player = Player(
                name = "{} {}".format(lines_part[0], lines_part[1]),
                age = lines_part[2],
                country = lines_part[3],
                money = lines_part[4]
            )

            players.append(player)
            print("Player: " + str(player))
            
        if not players:
            raise PlayersFileIsEmpty()

        print('Players file was read with {} players'.format(len(players)))
        return players