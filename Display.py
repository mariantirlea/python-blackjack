import os
from time import sleep
from utilities.Globals import Globals
from termcolor import colored

class Display:
    INTRO = \
"""
 ▄▄▄▄    ██▓     ▄▄▄       ▄████▄   ██ ▄█▀ ▄▄▄██▀▀▀ ▄▄▄       ▄████▄   ██ ▄█▀
▓█████▄ ▓██▒    ▒████▄    ▒██▀ ▀█   ██▄█▒    ▒██   ▒████▄    ▒██▀ ▀█   ██▄█▒ 
▒██▒ ▄██▒██░    ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░    ░██   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
▒██░█▀  ▒██░    ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▓██▄██▓  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
░▓█  ▀█▓░██████▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄ ▓███▒    ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
░▒▓███▀▒░ ▒░▓  ░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒ ▒▓▒▒░    ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
▒░▒   ░ ░ ░ ▒  ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ▒ ░▒░     ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
 ░    ░   ░ ░     ░   ▒   ░        ░ ░░ ░  ░ ░ ░     ░   ▒   ░        ░ ░░ ░ 
 ░          ░  ░      ░  ░░ ░      ░  ░    ░   ░         ░  ░░ ░      ░  ░   
      ░                   ░                                  ░               
"""

    CARD_TEMPLATE = \
"""
┌────────┐
│ VV     │
│ S      │
│        │
│      S │
│     VV │
└────────┘
"""
    __columns = 0
    __lines = 0

    __current_bet_player = 0
    __players_page_message = None

    def __init__(self, game):
        os.system('mode 135,35')
        # if Globals.COLORED:
            # os.system('color F0')
        self.__get_term_size()
        self.game = game
    
    def __get_term_size(self):
        term_size = os.get_terminal_size()
        self.__columns, self.__lines = term_size.columns, term_size.lines

        if Globals.DEBUG:
            print("{}x{}".format(self.__columns, self.__lines))

    def clear(self):
        os.system('cls')
        self.__get_term_size()

    def __draw_intro_with_delay(self, intro_lines, top_offset, left_offset, delay = 0):
        print('\n' * int(top_offset - 1))
                
        for intro_line in intro_lines:
            print(self.__center_line(self.__color_text(intro_line, Globals.TEXT_COLOR_HEADER)))

            sleep(delay)

    def show_intro(self):
        intro_lines = self.INTRO.strip().split("\n");

        intro_width = len(intro_lines[0])
        intro_height = len(intro_lines)

        if Globals.DEBUG:
            print(intro_width, intro_height)

        if (intro_width > self.__columns) or (intro_height > self.__lines):
            # os.system('mode '+ intro_width + ',' + intro_height)
            print("Blackjack")
        else:
            left_offset = (self.__columns - intro_width) / 2
            top_offset = (self.__lines - intro_height) / 2

            self.__draw_intro_with_delay(intro_lines, top_offset, left_offset, 0.03)
            
            for delay_index in range(Globals.INTRO_DELAY_IN_SECONDS):
                top_offset = (self.__lines - intro_height) / 2

                self.clear()
                self.__draw_intro_with_delay(intro_lines, top_offset, left_offset, 0)
                
                print()
                print(self.__center_line(Globals.AUTHOR))
                print("\n\n")

                print(self.__color_text(self.__center_line("Loading {}".format("." * (delay_index + 1))), Globals.TEXT_COLOR_HEADER))
                sleep(1)

    def __color_text(self, text, color):
        if Globals.COLORED:
            return colored(text, color)
        else:
            return text

    def show_help(self):
        self.clear()

        print(self.__center_multiple_lines((
            self.__color_text("Welcome to the Blackjack game implemented for the Python course.\n", Globals.TEXT_COLOR),
            self.__color_text("It is very easy to play ;) Enter the response for the questions on the interface itself\n", Globals.TEXT_COLOR),
            self.__color_text(" or use the special keyword: exit/restart at anytime during the game.\n", Globals.TEXT_COLOR),
            "\n",
            "\n",
            self.__color_text("Have fun and good luck!\n", "white"),
            "\n",
            "\n",
            self.__color_text("Press enter key to continue", "white")
        )))

        self.game.read_players_file()
        self.game.set_next_question_and_function(
            "", 
            self.show_players_page
        )

    def show_players_page(self, param):
        
        lines = [
            self.__color_text("Blackjack game will start with {} players".format(len(self.game.players)), Globals.TEXT_COLOR),
            "\n",
            "\n",
            "\n"
            "\n"
        ]
        
        for index in range(len(self.game.players)):
            player = self.game.players[index]

            bet_text = " bet {} chips".format(player.bet) if player.bet != 0 else " waiting for bet"
            if index == self.__current_bet_player:
                lines.append(self.__color_text(">>> {} ({}, {}){}\n".format(player.name, player.age, player.country, bet_text), "white"))
            else:
                lines.append(self.__color_text("{} ({}, {}){}\n".format(player.name, player.age, player.country, bet_text), "white"))

        lines.append("\n")
        lines.append("\n")
        lines.append("\n")

        if self.__players_page_message != None:
            lines.append(self.__players_page_message)

        print(self.__center_multiple_lines(lines))

        if(self.__current_bet_player == len(self.game.players)):

            print(self.__center_line(self.__color_text("All bets were placed! Press enter key to continue", "white")))
            
            self.game.set_next_question_and_function(
                "", 
                self.__draw_game
            )

        else:
            current_bet_player = self.game.players[self.__current_bet_player]
            self.game.set_next_question_and_function(
                self.__center_line(self.__color_text("{}, you have {} chips available. What is your bet for this game: ".format(current_bet_player.name, current_bet_player.chips), Globals.TEXT_COLOR)), 
                self.__on_bet_placed
            )
    
    def __draw_game(self, param):
        self.game.deck.create()
        self.game.deck.shuffle()

        self.draw_multiple_cards()

    def __on_bet_placed(self, param):
        self.__players_page_message = None

        if param.isdigit() and int(param) > 0 and int(param) <= self.game.players[self.__current_bet_player].chips:
            self.game.players[self.__current_bet_player].set_bet(int(param))
            self.__current_bet_player = self.__current_bet_player + 1
        else:
           self.__players_page_message = self.__color_text("Invalid bet. Please enter a value between {} and {}".format("1", str(self.game.players[self.__current_bet_player].chips)), Globals.TEXT_COLOR_HEADER) 

        self.show_players_page(None)

  
    def __center_multiple_lines(self, lines):
        whole_text = '\n' * int((self.__lines - len(lines)) / 2 - 1)

        for line in lines:
            whole_text = whole_text + self.__center_line(line)

        return whole_text

    def __center_line(self, line):
        left_offset = int((self.__columns - len(line)) / 2)
        
        return line.rjust(left_offset + len(line))

    def __draw_card(self, value = "A", sign = "♥"):
        return self.CARD_TEMPLATE.replace("VV", '{:2}'.format(value)).replace("S", sign)
        
    def draw_multiple_cards(self, cards = [
        {"value" : "A", "sign" : "♥"}, 
        {"value" : "10", "sign" : "♣"},
        {"value" : "10", "sign" : "♣"},
        {"value" : "10", "sign" : "♣"},
        {"value" : "10", "sign" : "♣"},
        {"value" : "10", "sign" : "♣"},
        {"value" : "10", "sign" : "♣"}

        ]):

        offset_x = 0

        result = ""

        for card in cards:
            rendered_card = self.__draw_card(card['value'], card['sign'])

            if result == "":
                result = rendered_card
            else:
                lines_rendered = rendered_card.strip().split("\n")
                lines_existing = result.strip().split("\n")

                result = ""
                for i in range(len(lines_existing)):
                    result = result + lines_existing[i][0 : offset_x] + lines_rendered[i] + "\n"

                print(result)

            offset_x = offset_x + 5

        print(result)


