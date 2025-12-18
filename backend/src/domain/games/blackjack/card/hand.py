
from .card import Card, Ace 

MAX_VALUE = 21

class Hand:
    def __init__(self):
        self.cards:list[Card] = []

    def add_card(self, card:Card):
        self.cards.append(card)
        return self.calculate_value()
    
    def calculate_value(self):
        aces = []
        value = 0
        for card in self.cards:
            if card.is_ace: aces.append(card)
            else: value += card.value

        value += self.handle_aces(aces)
        return value
    
    def handle_aces(self, aces:list[Ace]):
        is_alt_added = False
        value = 0
        for i in range(len(aces)):
            if (value + aces[i].alt_value <= MAX_VALUE) : 
                value += aces[i].alt_value
                is_alt_added = True
            elif is_alt_added :
                value -= aces[i-1].alt_value
                value += aces[i-1].value
                is_alt_added = False
                value += aces[i].value
            else: value += aces[i].value
        return value
    
    def __str__(self):
        if(self.cards):
            text = "Hand content: \n"
            for card in self.cards:
                text += f"\t{str(card)}\n"
            
            text += f"\n\tHand value: {self.calculate_value()}"

            return text
        else: return "Hand is empty"