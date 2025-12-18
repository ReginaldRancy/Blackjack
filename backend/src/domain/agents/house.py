from .agentBase import AgentBase, Description

class House(AgentBase):
    def __init__(self):
        super().__init__(
            Description(
                name="House",
                balance=0.0,
                is_infinite_balance=True
            )
        )