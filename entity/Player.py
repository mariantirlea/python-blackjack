
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
        self.__calculate_value()

    def __calculate_value(self):

        self.__value = 0
        for card in self.__hand:

            if card.value in "2 3 4 5 6 7 8 9".split(" "):
                self.__value = self.__value + int(card.value)
            elif card.value in "10 J Q K".split(" "):
                self.__value = self.__value + 10
            else:
                if self.__value + 11 <= 21:
                    self.__value = self.__value + 11
                else:
                    self.__value = self.__value + 1

    def get_hand(self):
        return self.__hand

    def get_value(self):
        return self.__value

    def display_hand(self):
        for card in self.__hand:
            print(str(card))

    def __str__(self):
        return "Player [{}, {}, {}, {}]".format(self.name, self.age, self.country, self.chips)
