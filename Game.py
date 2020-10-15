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
        self.__display = Display()

    def __set_next_question_and_function(self, question, function):
        self.__next_question = question
        self.__next_function = function

    def __exit(self): 
        self.__active = False
        print('Game will exit now...')
        sleep(0.2)

    def __read_players_file(self):

        try:
            self.players = FileUtils.read_players_file(self.PLAYERS_FILE_LOCATION)

        except (PlayersFileNotFound, PlayersFileIsEmpty) as e:
            print(e.message)
            self.__exit()

    def __start_game_with_players(self, number_of_players):
        print("Number of players: " + number_of_players)

        self.__display.draw_multiple_cards()
        # self.__exit()

    def __check_response_players_file(self, param):
        if param.lower() == 'y' or param == "":
            self.__read_players_file()

            self.__set_next_question_and_function(
                "How many players you want to start with: ", 
                self.__start_game_with_players
            )

        elif param.lower() == 'n':
            print('Closing the game. Players file was not read.')
            self.__exit()
        else:
            print('Invalid option! Correct values (Y/n)')

    def __execute_game(self): 
       
        self.__set_next_question_and_function(
            "Do you want to read the players file? (Y/n) ", 
            self.__check_response_players_file
        )

    def start(self):
        self.__display.show_intro()
        self.__display.clear()
        
        print("Started")
        sleep(0.2)

        self.__execute_game()

        while self.__active:
            user_input = input(self.__next_question)
            os.system('cls')

            if user_input == 'exit':
                self.__exit()
                break
            elif user_input == 'restart':
                self.start()
                break

            self.__display.clear()
            if self.__next_function != None:
                self.__next_function(user_input)

