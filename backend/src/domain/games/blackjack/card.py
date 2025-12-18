
# class HouseDescription:
#     inGameBalance: float
#     cards:list[Card] = defaultCardList
#     usedCards: list[Card] = []

















class Card:
    def __init__(self, symbol:str, val:int):
        self.symbol = symbol
        self.value = val
        self.is_ace = False

class Ace(Card):
    def __init__(self):
        super().__init__("A", 1)
        self.is_ace = True
        self.ace_val = 11

defaultCardList = [
        Ace(), Ace(), Ace(), Ace(),

        Card("2", 2), Card("2", 2), Card("2", 2), Card("2", 2),

        Card("3", 3), Card("3", 3), Card("3", 3), Card("3", 3),

        Card("4", 4), Card("4", 4), Card("4", 4), Card("4", 4),

        Card("5", 5), Card("5", 5), Card("5", 5), Card("5", 5),

        Card("6", 6), Card("6", 6), Card("6", 6), Card("6", 6),

        Card("7", 7), Card("7", 7), Card("7", 7), Card("7", 7),

        Card("8", 8), Card("8", 8), Card("8", 8), Card("8", 8),

        Card("9", 9), Card("9", 9), Card("9", 9), Card("9", 9),

        Card("10", 10), Card("10", 10), Card("10", 10), Card("10", 10),

        Card("J", 10), Card("J", 10), Card("J", 10), Card("J", 10),

        Card("Q", 10), Card("Q", 10), Card("Q", 10), Card("Q", 10),

        Card("K", 10), Card("K", 10), Card("K", 10), Card("K", 10)
]