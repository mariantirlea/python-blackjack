
from manager.Game import Game
from manager.GameState import GameState
from entity.Deck import Deck
from entity.Player import Player
from manager.Display import Display

if __name__ == "__main__":

    # d = Deck()

    # d.create()
    # d.shuffle()

    # print(d.pick_card())
    # print(d.pick_card())
    # print(d.pick_card())
    # print(d.pick_card())

    # p = Player('', 22, '', 222)

    # p.pick_card(d)
    # p.pick_card(d)
    # p.pick_card(d)
    # p.pick_card(d)

    # p.display_hand()

    g = Game()
    d = Display(g)

    # p1 = Player("John Snow", 20, "Romania", 200)
    # p2 = Player("John Snow", 20, "Romania", 200)
    # p3 = Player("John Snow", 20, "Romania", 200)
    # p4 = Player("John Snow", 20, "Romania", 200)

    # gs.players = [p1, p2, p3, p4]

    # remove these 2 lines
    # g.state.deck.create()
    # g.state.deck.shuffle()
    g.state.read_players_file()

    g.state.deck.create()
    g.state.deck.shuffle()

    g.state.players[0].pick_card(g.state.deck)
    g.state.players[0].pick_card(g.state.deck)
    g.state.players[0].pick_card(g.state.deck)
    g.state.players[0].pick_card(g.state.deck)

    g.state.players[1].pick_card(g.state.deck)
    g.state.players[2].pick_card(g.state.deck)
    g.state.players[3].pick_card(g.state.deck)


    # g.state.players = g.state.players[:-3]

    # for p in g.state.players:
    #     print("player....." + str(p))
    #     for c in p.get_hand():
    #         print(str(c))

    d.draw_game_state()
