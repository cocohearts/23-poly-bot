from getinfo import *
from battles import *
from time import sleep
import random
from strategy import *
import datetime
from math import log

fired = bool(input("fought today yet? (y/empty)"))
if fired:
    print("pausing until 4pm")
    waittime = datetime.datetime.now()
    waittime = waittime.replace(hour=16,minute=0,second=0)
    pause.until(waittime)

cash = getCash()

while True:
    try:
        battles = getBattles()
    except:
        sleep(120)
        continue

    beststrategy = None
    bestEV = 0
    start = datetime.datetime.now()
    for battle in battles:
        print(battle.name)
        strategy = Strategy.battleSolver(battle,cash)
        if strategy.value > bestEV:
            beststrategy = strategy
            bestEV = strategy.value

    now = datetime.datetime.now()
    elapsed_hours = (now+datetime.timedelta(hours=8)).hour
    cutoff = 0.07*(log(26-elapsed_hours))**(0.5)
    try:
        print("time elapsed",datetime.datetime.now()-start)
        print("bestEV:",bestEV,beststrategy.battle.name)
    except:
        pass
    if bestEV > cutoff:
        try:
            cash = beststrategy.execute()
        except:
            pass

    sleep(200+random.randint(1,200))