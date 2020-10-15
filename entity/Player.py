
class Player:

    def __init__(self, name, age, country, money):
        self.name = name
        self.age = age
        self.country = country
        self.money = money

    def __str__(self):
        return "Player [{}, {}, {}, {}]".format(self.name, self.age, self.country, self.money)