

class Card:
    def __init__(self, symbol:str, value:int, color:str):
        self.symbol = symbol
        self.value = value
        self.color = color
        self.is_ace = False
        self.is_visible = False

    def __str__(self):
        if self.is_visible:
            return f"Card: {self.symbol}:{self.color}"
        else :
            return f"Card is hidden"

class Ace(Card):
    def __init__(self,symbol:str, value:int, color:str):
        super().__init__(symbol, value, color)
        self.is_ace = True
        self.is_visible = False
        self.alt_value = 11

    def __str__(self):
        return super().__str__()

