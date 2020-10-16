
from entity.Deck import Deck
from entity.Player import Player

if __name__ == "__main__":

    d = Deck()

    d.create()
    d.shuffle()

    print(d.pick_card())
    print(d.pick_card())
    print(d.pick_card())
    print(d.pick_card())

    p = Player('', 22, '', 222)

    p.pick_card(d)
    p.pick_card(d)
    p.pick_card(d)
    p.pick_card(d)

    p.display_hand()


