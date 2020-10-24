
class Player:

    def __init__(self, name, age, country, chips):
        self.name = name
        self.age = age
        self.country = country
        self.chips = chips
        self.bet = 0
        self.__hand = []
        self.__value = 0
        self.stand = False
        self.won = False
        self.exceeded = False

    def set_bet(self, bet):
        self.bet = bet
        self.chips = self.chips - self.bet

    def pick_card(self, deck):
        self.__hand.append(deck.pick_card())
        self.__calculate_value()
        self.__chech_score()


    def __chech_score(self):
        if self.__value == 21:
            self.won = True

        if self.__value > 21:
            self.exceeded = True

    def __calculate_value(self):

        self.__value = 0
    
        aces_found = 0
        for card in self.__hand:

            if card.value in "2 3 4 5 6 7 8 9 10".split(" "):
                self.__value = self.__value + int(card.value)
            elif card.value in "J Q K".split(" "):
                self.__value = self.__value + 10
            else:
                self.__value = self.__value + 11
                aces_found = aces_found + 1

        for index in range(aces_found):
            if self.__value <= 21:
                break

            self.__value = self.__value - 10

    def get_hand(self):
        return self.__hand

    def clear_hand(self):
        self.__hand = []

    def get_value(self):
        return self.__value

    def display_hand(self):
        for card in self.__hand:
            print(str(card))

    def __str__(self):
        return "Player [{}, {}, {}, {}, Hand value: {}, Stand: {}, Exceeded: {}, Won: {}]".format(self.name, self.age, self.country, self.chips, self.__value, self.stand, self.exceeded, self.won)
