
class Player:

    def __init__(self, name, age, country, chips):
        self.name = name
        self.age = age
        self.country = country
        self.chips = chips
        self.bet = 0

    def __str__(self):
        return "Player [{}, {}, {}, {}]".format(self.name, self.age, self.country, self.chips)

    def set_bet(self, bet):
        self.bet = bet