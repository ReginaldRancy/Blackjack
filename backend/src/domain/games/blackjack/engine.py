from domain.agents.bot import Bot
from domain.agents.house import House
from domain.agents.player import Player
from domain.agents.agentBase import Description, AgentBase, DrawContext
from domain.games.blackjack.card.deck import Deck
from domain.games.blackjack.bet.bet import Bet
from domain.games.blackjack.card.hand import Hand
from enum import Enum

from pathlib import Path
BASE_DIR = Path(__file__).parent


MIN_BETTING_AMOUNT = 2
DEFAULT_N_DECK = 6
HOUSE_DRAW_MIN = 17
BLACKJACK_VALUE = 21
INITIAL_MAX_BET = 5

class GameState(Enum):
    BETTING = 1
    DEALING = 2
    PLAYER_TURN = 3
    HOUSE_TURN = 4
    RESOLUTION = 5

class Engine:

    def __init__(self, house:House, player:Player) -> None:
        self.house = house
        self.agents:list[AgentBase] = [player]
        self.deck:Deck | None = None
        self.hands:list[Hand] = []
        self.house_hand = Hand(house, None)
        self.gameState = GameState.BETTING


    def start_game(self, n_bots = 0):
        for i in range(n_bots):
            self.agents.append(Bot(Description(f"Bot-{i + 1}")))
        
        self.play_round()

    def play_round(self):
        self.gameState  = GameState.BETTING
        if self.deck == None: self.deck = Deck(max(len(self.agents), DEFAULT_N_DECK))
        self.collect_bets()

        self.gameState = GameState.DEALING
        self.deck.shuffle()
        self.deal_first_cards()

        self.gameState = GameState.PLAYER_TURN
        self.deal_extra_cards()

        self.gameState = GameState.HOUSE_TURN
        self.deal_to_house()

        self.gameState = GameState.RESOLUTION
        self.resolve_round()
    
    def collect_bets(self):
        for agent in self.agents:
            continue_betting = True
            max_hands = INITIAL_MAX_BET
            while(continue_betting):
                
                if agent.can_bet(MIN_BETTING_AMOUNT) == False: continue_betting = False
                elif max_hands == 0: continue_betting = False
                else :
                    new_bet_amount = agent.bet()
                    max_hands -= 1
                    if new_bet_amount > MIN_BETTING_AMOUNT:
                        bet = Bet(new_bet_amount)
                        self.hands.append(Hand(agent, bet))
                    else : continue_betting = False

    def __str__(self):
        text = "_"*50 + "\n"
        text += "Black Jack game\n\n"
        text += str(self.house_hand)
        text += "Participants:\n"
        for agent in self.agents:
            text += "- " + str(agent) + "\n"
        text += "\nHands on the table:\n"
        for hand in self.hands:
            text+= str(hand)+"\n\n"

        return text
    
    def deal_first_cards(self):
        if self.deck == None: self.deck = Deck(max(len(self.agents), DEFAULT_N_DECK))
        for i in range(2):
            for j in range(len(self.hands)):
                self.hands[j].add_card(self.deck.deal_card())
                if self.hands[j].is_blackjack(): 
                    self.manage_blackjack(self.hands[j])
            self.house_hand.add_card(self.deck.deal_card(False))
        print(self)

    def deal_extra_cards(self):
        h_hand = self.house_hand
        if(self.deck):
            for hand in self.hands:
                draw = True
                while draw:
                    context = DrawContext(hand.calculate_value(), h_hand.calculate_value())
                    want_to_draw = hand.agent.decide_draw(context)
                    if hand.can_draw(h_hand) and want_to_draw:
                        hand.add_card(self.deck.deal_card())
                        print(f"Your new hand is:\n{str(hand)}")  #11########## Important à changer éventuellement
                    else :
                        draw = False
            print(self)
        else: raise Exception("No deck")

    def deal_to_house(self):
        if self.deck == None : return
        self.house_hand.reveal_hidden()
        print(self.house_hand)

        while(self.house_hand.calculate_value() < HOUSE_DRAW_MIN):
            self.house_hand.add_card(self.deck.deal_card())
            print(self.house_hand)

    def resolve_round(self):
        house_score = self.house_hand.calculate_value()
        if house_score > BLACKJACK_VALUE:
            for hand in self.hands:
                hand.resolve()
            self.hands = []
        else:
            for hand in self.hands:
                hand.resolve(house_score)
            self.hands = []
        self.house_hand = Hand(self.house, None)
            
    def manage_blackjack(self, hand:Hand):
        pass
        ## À déplacer et implémenter dans rules
