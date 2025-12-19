from domain.agents.agentBase import AgentBase, Description

class House(AgentBase):
    def __init__(self, name="House"):
        super().__init__(
            Description(
                name=name,
                balance=0.0,
                is_house=True
            )
        )