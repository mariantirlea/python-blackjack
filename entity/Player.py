
class Player:

    def __init__(self, name, age, country, chips):
        self.name = name
        self.age = age
        self.country = country
        self.chips = chips
        self.bet = 0
        self.__hand = []
        self.__value = 0

    def set_bet(self, bet):
        self.bet = bet
        self.chips = self.chips - self.bet

    def pick_card(self, deck):
        self.__hand.append(deck.pick_card())

    def get_hand(self):
        return self.__hand

    def get_value(self):
        return self.__value

    def display_hand(self):
        for card in self.__hand:
            print(str(card))

    def __str__(self):
        return "Player [{}, {}, {}, {}]".format(self.name, self.age, self.country, self.chips)
