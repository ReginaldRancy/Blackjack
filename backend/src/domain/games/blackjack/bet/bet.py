class Bet:
    def __init__(self, amount: int):
        self.amount = amount

    def __str__(self):
        return f"{self.amount}$"