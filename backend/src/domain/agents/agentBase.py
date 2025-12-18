from dataclasses import dataclass

@dataclass
class Description:
    name:str
    balance:float
    is_infinite_balance:bool = False


class AgentBase:
    def __init__(self, description:Description):
        self.description = description

    def adjust_balance(self, new_balance:float):
        self.description.balance = new_balance

    def __str__(self):
        return f"Name: {self.description.name}, Balance: {self.description.balance}"