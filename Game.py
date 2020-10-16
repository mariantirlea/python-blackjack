from time import sleep
import os

from Display import Display
from entity.Player import Player
from utilities.FileUtils import FileUtils
from utilities.Exceptions import PlayersFileNotFound, PlayersFileIsEmpty

class Game:

    PLAYERS_FILE_LOCATION = "data/ListaParticipanți.txt"

    __active = True

    __next_question = ""
    __next_function = None

    def __init__(self):
        self.__display = Display(self)

    def set_next_question_and_function(self, question, function):
        self.__next_question = question
        self.__next_function = function

    def __exit(self): 
        self.__active = False
        print('Game will exit now...')
        sleep(0.2)

    def read_players_file(self):

        try:
            self.players = FileUtils.read_players_file(self.PLAYERS_FILE_LOCATION)

        except (PlayersFileNotFound, PlayersFileIsEmpty) as e:
            print(e.message)
            sleep(2)
            self.__exit()

    def start(self):
        self.__display.show_intro()
        self.__display.show_help()
      
        while self.__active:
            user_input = input(self.__next_question)
            os.system('cls')

            if user_input == 'exit':
                self.__exit()
                break
            elif user_input == 'restart':
                self.__display.clear()
                self.start()
                break

            self.__display.clear()
            if self.__next_function != None:
                self.__next_function(user_input)

