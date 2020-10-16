import random

from utilities.Globals import Globals
from entity.Card import Card, CardType


class Deck:

    def __init__(self):
        self.__PACKAGE = []

    def create(self):
        for card_type in CardType:
            for card_value in Card.VALUES:
                self.__PACKAGE.append(Card(card_value, card_type))

        # print(str(self))

    def shuffle(self):
        random.shuffle(self.__PACKAGE)
        # print(str(self))

    def pick_card(self):
        return self.__PACKAGE.pop()

    def __str__(self):
        text = ""
        for card in self.__PACKAGE:
            text = text + "({} {}) ".format(card.value,
                                            card.card_type.value[0]['sign'])
        return "Deck [{}]".format(text)
