from domain.agents.house import House, Description
from domain.agents.player import Player
from domain.agents.bot import Bot

from domain.games.blackjack.card.deck import Deck
from domain.games.blackjack.card.hand import Hand
from domain.games.blackjack.card.card import Card, Ace
from domain.games.blackjack.engine import Engine

# elements = [
#     Player(Description("Player", 200.0)),
#     Bot(Description("Bot-1", 200.0)),
#     Bot(Description("Bot-2", 200.0)),
#     Bot(Description("Bot-3", 200.0)),
#     House()
# ]

# for element in elements :
#     print(element)
#     element.adjust_balance(31231.0)


# hand = Hand()
# ace1 = Ace("A", 1, "C")
# ace2 = Ace("A", 1, "H")
# card1 = Card("7",7,"H")
# card2 = Card("3",3, "S")
# card3 = Card("K", 10, "D")


# (hand.add_card(card1))
# (hand.add_card(card2))
# (hand.add_card(ace1))
# (hand.add_card(ace2))
# (hand.add_card(card3))
# print(hand)

house = House()
player = Player(Description("Monique", 200))
engine = Engine(house, player)
engine.start_game(2)
print(engine)