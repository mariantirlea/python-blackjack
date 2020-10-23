import unittest


from entity.Player import Player
from entity.Card import Card, CardType


class FakeDeck:
    def __init__(self):
        self.__PACKAGE = []

    def set_cards(self, cards):
        self.__PACKAGE = cards

    def pick_card(self):
        return self.__PACKAGE.pop()


class TestPlayerMethods(unittest.TestCase):

    def setUp(self):
        self.player = Player(name="Player 1", age=0,
                             country="Romania", chips=0)
        self.fake_deck = FakeDeck()

    def tearDown(self):
        self.fake_deck.set_cards([])

    def prepare_cards(self, card_values):
        cards_from_values = list(map(lambda element: (
            Card(element, CardType.SPADES)
        ), card_values))

        self.fake_deck.set_cards(cards_from_values)

        for index in range(len(cards_from_values)):
            self.player.pick_card(self.fake_deck)

    # @unittest.skip
    def test_with_special_cards(self):
        self.prepare_cards(["J", "Q", "K"])

        self.assertEqual(self.player.get_value(), 30)

    def test_with_card_A_as_1(self):
        self.prepare_cards(["K", "K", "A"])

        self.assertEqual(self.player.get_value(), 21)

    def test_with_card_A_as_11(self):
        self.prepare_cards(["1", "2", "A"])
        self.assertEqual(self.player.get_value(), 14)

    def test_with_card_two_A_as_1(self):
        self.prepare_cards(["A", "9", "1", "A"])
        self.assertEqual(self.player.get_value(), 12)

    def test_with_card_multiple_A_one_as_11(self):
        self.prepare_cards(["A", "2", "1", "A", "6"])
        self.assertEqual(self.player.get_value(), 21)

    def test_with_normal_cards(self):
        self.prepare_cards(["2", "3", "4", "5", "6", "7", "8", "9", "10"])

        self.assertEqual(self.player.get_value(), 54)
