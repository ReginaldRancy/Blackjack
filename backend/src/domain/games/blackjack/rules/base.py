## Manage blackjack
## Manage insurance
## Manage splitting
## Manage doubling_down
## Strategy

from abc import ABC, abstractmethod
from domain.games.blackjack.card.hand import Hand


class BlackjackRuleSet(ABC):

    @abstractmethod
    def handle_blackjack(self, hand: Hand, hands:list[Hand]) -> bool:
        pass

    @abstractmethod
    def can_insure(self, hand: Hand, house_hand: Hand) -> bool:
        pass

    @abstractmethod
    def resolve_insurance(self, hand: Hand, house_hand: Hand):
        pass

    @abstractmethod
    def can_split(self, hand: Hand) -> bool:
        pass

    @abstractmethod
    def split(self, hand: Hand):
        pass

    @abstractmethod
    def can_double_down(self, hand: Hand) -> bool:
        pass
    