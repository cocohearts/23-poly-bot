from getinfo import *
from send_msg import main
from battles import *
from time import sleep
import random

class Strategy:
    def __init__(self,battlename,number,strategy,logEV):
        self.battlename = battlename
        self.number = number
        self.strategy = strategy
        self.value = logEV

    def battleSolver(mybattle,cash):
        if mybattle.defender.cost() < 2 * cash:
            if mybattle.level in [5,10]:
                if mybattle.defender.armydict['defender'] == 0:
                    # giants only
                    top = cash//Army.costdict['giant']
                    print(top)
                    maxlogEV = 0
                    giantnumber = 0
                    for giantcount in range(0,top+1):
                        mybattle.attacker.armydict['giant'] = giantcount
                        battleresults = mybattle.battlelogEV(cash)
                        if battleresults[1] >= 0.8 and battleresults[0] > maxlogEV:
                            giantnumber = giantcount
                            maxlogEV = battleresults[0]
                    print(maxlogEV)
                    return Strategy(mybattle.name,giantnumber,"giant",maxlogEV)
                elif mybattle.defender.armydict['cloak'] == 0:
                    top = cash//Army.costdict['battleship']
                    maxlogEV = 0
                    battleshipnumber = 0
                    for battleshipcount in range(0,top+1):
                        mybattle.attacker.armydict['battleship'] = battleshipcount
                        battleresults = mybattle.battlelogEV(cash)
                        if battleresults[1] >= 0.8 and battleresults[0] > maxlogEV:
                            battleshipnumber = battleshipcount
                            maxlogEV = battleresults[0]
                    print(maxlogEV)
                    return Strategy(mybattle.name,battleshipnumber,"battleship",maxlogEV)
        
        return None