from domain.agents.agentBase import AgentBase, Description

class Player(AgentBase):
    def __init__(self, description: Description):
        super().__init__(description)
        self.is_player = True

    def bet(self):
        print(f"(Player) {self.name}, your balance is {self.balance}$") 
        try:
            amount = int(input("How much do You wand to bet? (0 to stop betting) --> "))
        except:
            amount = 0
        if amount > self.balance: amount = int(self.balance)
        return super().bet(amount)
