

class Card:
    def __init__(self, symbol:str, value:int, color:str):
        self.symbol = symbol
        self.value = value
        self.color = color
        self.is_ace = False

    def __str__(self):
        return f"Card: {self.symbol}:{self.color}"

class Ace(Card):
    def __init__(self,symbol:str, value:int, color:str):
        super().__init__(symbol, value, color)
        self.is_ace = True
        self.alt_value = 11

    def __str__(self):
        return super().__str__()

