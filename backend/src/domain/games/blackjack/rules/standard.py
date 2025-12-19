from domain.games.blackjack.rules.base import BlackjackRuleSet
from domain.games.blackjack.card.card import Ace
from domain.games.blackjack.card.hand import Hand


class StandardBlackjackRules(BlackjackRuleSet):

    def handle_blackjack(self, hand: Hand, hands:list[Hand]) -> bool:
        if hand.is_blackjack():
            hands.remove(hand)
            print(f"\n{hand.agent.name} got a Blackjack !\n")
            hand.resolve()
            return True
        return False

    def can_insure(self, hand: Hand, house_hand: Hand) -> bool:
        return False

    def resolve_insurance(self, hand: Hand, house_hand: Hand):
        pass

    def can_split(self, hand: Hand) -> bool:
        return False

    def split(self, hand: Hand):
        pass

    def can_double_down(self, hand: Hand) -> bool:
        return False