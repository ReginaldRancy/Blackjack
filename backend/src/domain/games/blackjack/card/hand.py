
from domain.games.blackjack.card.card import Card, Ace 
from domain.games.blackjack.bet.bet import Bet
from domain.agents.agentBase import AgentBase

import math
from enum import Enum

BLACKJACK_VALUE = 21
RE_DRAW_MAX = 12
ACE_ALT_BOOST = 10

class Outcome(Enum):
    LOSE = 0
    PUSH = 1
    WIN = 2
    BLACKJACK = 3


class Hand:
    def __init__(self, agent:AgentBase, bet: Bet|None):
        self.agent = agent
        self.bet = bet
        self.cards:list[Card] = []

    def add_card(self, card:Card):
        if(self.bet == None) and (len(self.cards) == 1): card.is_visible = True
        self.cards.append(card)
        return self.calculate_value()
    
    def calculate_value(self):
        value = sum(card.value for card in self.cards if card.is_visible)
        aces = self.count_aces()
        while (aces > 0) and value + ACE_ALT_BOOST <= BLACKJACK_VALUE:
            value += ACE_ALT_BOOST
            aces -= 1

        return value
        
    def __str__(self):
        name = self.agent.name
        if self.agent.is_player : name = "(Player) " + name
        if(self.cards):
            text = f"- {name}'s hand content: \n"
            for card in self.cards:
                text += f"\t{str(card)}\n"
            
            text += f"\n\tHand value: {self.calculate_value()}"
            if self.bet: text += f"\n\tBet: {str(self.bet)}"

            return text + "\n"
        else: return f"{name}'s hand is empty, \n\tBet: {str(self.bet)}"

    def can_draw(self, house):
        return self.calculate_value() < BLACKJACK_VALUE
        
    
    def reveal_hidden(self):
        for card in self.cards:
            card.is_visible = True

    def count_aces(self):
        aces = 0
        for card in self.cards:
            if card.is_ace and card.is_visible:
                aces += 1
        return aces
    
    def is_blackjack(self):
        return (len(self.cards)== 2) and (self.calculate_value() == BLACKJACK_VALUE)
    
    def resolve(self, house_score: int = 0):
        if not self.bet:
            raise Exception("No bet")

        score = self.calculate_value()

        if self.is_blackjack():
            self.agent.gain(self.payout_blackjack(self.bet.amount))
            return

        if score > BLACKJACK_VALUE:
            outcome = Outcome.LOSE
        elif house_score > BLACKJACK_VALUE:
            outcome = Outcome.WIN
        elif score > house_score:
            outcome = Outcome.WIN
        elif score == house_score:
            outcome = Outcome.PUSH
        else:
            outcome = Outcome.LOSE

        match outcome:
            case Outcome.LOSE:
                payout = self.payout_lose(self.bet.amount)
            case Outcome.PUSH:
                payout = self.payout_push(self.bet.amount)
            case Outcome.WIN:
                payout = self.payout_win(self.bet.amount)

        self.agent.gain(payout)


    def payout_lose(self, bet: int) -> int:
        return 0

    def payout_push(self, bet: int) -> int:
        return bet

    def payout_win(self, bet: int) -> int:
        return bet * 2

    def payout_blackjack(self, bet: int) -> int:
        return bet + (bet * 3) // 2