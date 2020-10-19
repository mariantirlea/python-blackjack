from utilities.Globals import Globals
from manager.Display import Display
from enum import Enum


class CardType(Enum):
    SPADES = {'sign': "♠", 'color': Globals.CARD_BLACK},
    DIAMONDS = {'sign': "♦", 'color': Globals.CARD_RED},
    HEARTS = {'sign': "♥", 'color': Globals.CARD_RED},
    CLUBS = {'sign': "♣", 'color': Globals.CARD_BLACK},


class Card:

    CARD_TEMPLATE_BACK = \
"""
┌────────┐
│XXXXXXXX│
│XXXXXXXX│
│XXXXXXXX│
│XXXXXXXX│
│XXXXXXXX│
└────────┘
"""

    CARD_TEMPLATE = \
"""
┌────────┐
│ VL     │
│ S      │
│        │
│      S │
│     VR │
└────────┘
"""

    VALUES = tuple("A 2 3 4 5 6 7 8 9 10 J Q K".split(' '))

    def __init__(self, value, card_type):
        if not isinstance(value, str):
            raise TypeError

        if not isinstance(card_type, CardType):
            raise TypeError

        self.value = value
        self.card_type = card_type

    def create(self, value, card_type):
        self.__init__(value, card_type)

    def __str__(self):
        return "Card [{}, {}]".format(self.value, self.card_type)

    def draw(self):

        lines = self.CARD_TEMPLATE.replace("VL", self.value.ljust(2)).replace("VR", self.value.rjust(2)).replace("S", self.card_type.value[0]['sign']).split("\n")
        lines = map(lambda element: (Display.color_text(element, self.card_type.value[0]['color'])), lines)

        return "\n".join(lines)