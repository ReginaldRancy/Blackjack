from .card import Card, Ace

from pathlib import Path
import random
import json

BASE_DIR = Path(__file__).parent
DEFAULT_PATH = BASE_DIR/"cards.json"

class Deck():
    
    def __init__(self, n_players:int = 1):
        self.n_players = n_players
        self.cards = self.initCards()*n_players
        self.usedCard = []

    def initCards(self):

        with open(DEFAULT_PATH) as f:
            cards = f.read()
            json_deck = json.loads(cards)
            deck = []
            for c in json_deck:
                if c["symbol"] == "A":
                    deck.append(Ace(c["symbol"], c["value"], c["color"]))
                else :
                    deck.append(Card(c["symbol"], c["value"], c["color"]))

            return deck
        
    def shuffle_deck(self):
        if len(self.usedCard) >= len (self.cards):
            for card in self.usedCard:
                self.cards.append(card)
                self.usedCard.remove(card)
            random.shuffle(self.cards)
            pass
        else:
            random.shuffle(self.cards)

    def __str__(self):
        text = "Content of the deck:\n"
        for card in self.cards:
            text += "\t" + str(card) + "\n"

        return text

