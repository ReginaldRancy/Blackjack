from domain.games.blackjack.card.card import Card, Ace

from pathlib import Path
import random
import json

BASE_DIR = Path(__file__).parent
DEFAULT_PATH = BASE_DIR/"cards.json"

class Deck():
    
    def __init__(self, n_decks:int):
        self.n_decks = n_decks
        self.cards:list[Card] = []
        for _ in range(self.n_decks):
            self.cards.extend(self.init_cards())
        self.used_card:list[Card] = []

    def init_cards(self):

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
        
    def shuffle(self):
        if len(self.used_card) >= len (self.cards):
            for card in self.used_card:
                self.cards.append(card)
                self.used_card.remove(card)
            random.shuffle(self.cards)
            pass
        elif len(self.used_card) == 0:
            random.shuffle(self.cards)

    def __str__(self):
        text = "Content of the deck:\n"
        for card in self.cards:
            text += "\t" + str(card) + "\n"


        return text
    
    def deal_card(self, make_visible = True):
        card = self.cards.pop()
        card.is_visible = make_visible
        self.used_card.append(card)
        return card
        

