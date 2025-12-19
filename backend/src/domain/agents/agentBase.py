
from dataclasses import dataclass
import math

@dataclass
class Description:
    name:str
    balance:float = 200.0
    is_player:bool = False
    is_house:bool = False


@dataclass
class DrawContext:
    hand_value: int
    house_value: int

class AgentBase:
    def __init__(self, description:Description):
        self.name = description.name
        self.balance = description.balance
        self.is_player = description.is_player
        self.is_house = description.is_house

    def adjust_balance(self, new_balance:float):
        self.balance = new_balance

    def __str__(self):
        text = "Player" if self.is_player else ""
        return f"Name: {self.name + text}, Balance: {self.balance}"
    
    def can_bet(self, minAmount:int):
        if self.balance < minAmount : return False
        return True
    
    def bet(self, amount = -1):
        if (amount == -1) : amount = math.floor(self.balance) #*15/100)
        self.balance -= amount
        return amount

    def decide_draw(self, ctx:DrawContext):
        if(ctx.hand_value >= 21): return False
        elif self.is_player:
            answer = input(f"House hand is worth {(ctx.house_value)}\n"
                           f"Your hand is worth {ctx.hand_value})\n"
                           "Do you want to draw? (Y/N) ")
            return answer.upper() == "Y"
        elif ctx.hand_value <= 11: return True
        elif ctx.hand_value >= 16: return False
        elif (3 <= ctx.house_value <= 6): return True
        return False

    def gain(self, amount:int):
        if self.is_house: return
        self.balance += amount
