from getinfo import *
from battles import *
from time import sleep
import random
from strategy import *
import datetime

cash = getCash()

while True:
    battles = getBattles()

    beststrategy = None
    bestEV = 0
    for battle in battles:
        print(battle.name)
        strategy = Strategy.battleSolver(battle,cash)
        if strategy.value > bestEV:
            beststrategy = strategy
            bestEV = strategy.value

    now = datetime.datetime.now()
    elapsed_hours = (now+datetime.timedelta(hours=8)).hour
    cutoff = 0.06 + 0.75*(24-elapsed_hours)
    if bestEV > cutoff or (now.hour == 15 and now.minute >= 30):
        if bestEV > 0:
            cash = beststrategy.execute()

    sleep(300+random.randint(1,300))