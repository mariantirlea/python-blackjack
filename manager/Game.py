from manager.GameState import GameState
from time import sleep
import os

from manager.Display import Display
from entity.Player import Player


class Game:

    __active = True
    __next_question = ""
    __next_function = None

    def __init__(self):
        self.__display = Display(self)
        self.state = GameState(self)

    def set_next_question_and_function(self, question, function):
        self.__next_question = question
        self.__next_function = function

    def exit(self):
        self.__active = False
        print('Game will exit now...')
        sleep(0.5)

    def start(self):
        self.__display.show_intro()
        self.__display.show_help()

        while self.__active:
            user_input = input(self.__next_question)
            self.__display.clear()

            if user_input == 'exit':
                self.exit()
                break
            elif user_input == 'restart':
                self.__display.clear()
                self.state.reset()
                self.start()
                break

            self.__display.clear()
            if self.__next_function != None:
                self.__next_function(user_input)
