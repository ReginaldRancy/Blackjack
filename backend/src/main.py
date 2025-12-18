from domain.agents.house import House, Description
from domain.agents.player import Player
from domain.agents.bot import Bot

elements = [ 
    Player(Description("Player", 200.0)),
    Bot(Description("Bot-1", 200.0)),
    Bot(Description("Bot-2", 200.0)),
    Bot(Description("Bot-3", 200.0)),
    House()
]

for element in elements :
    print(element)
    element.adjust_balance(31231.0)
