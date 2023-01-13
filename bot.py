from getinfo import *
from send_msg import main
from battles import *
from time import sleep
import random
from strategy import *

while True:
    battles = getBattles()

    beststrategy = None
    bestEV = 0
    for battle in battles:
        print(battle.name)
        strategy = Strategy.battleSolver(battle,447)
        if strategy:
            if strategy.value > bestEV:
                beststrategy = strategy
                bestEV = strategy.value
    if bestEV > 0.16:
        main(" ".join(["buy",beststrategy.strategy,str(beststrategy.number)]),"token.txt")
        sleep(5)
        main(" ".join(["battle",beststrategy.battlename,"all"]),"token.txt")