
class Player:

    hand = []

    def __init__(self, name, age, country, chips):
        self.name = name
        self.age = age
        self.country = country
        self.chips = chips
        self.bet = 0

    def set_bet(self, bet):
        self.bet = bet
        self.chips = self.chips - self.bet

    def pick_card(self, deck):
        self.hand.append(deck.pick_card())

    def display_hand(self):
        for card in self.hand:
            print(str(card))

    def __str__(self):
        return "Player [{}, {}, {}, {}]".format(self.name, self.age, self.country, self.chips)
