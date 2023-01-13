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
        if mybattle.defender.cost() < cash and mybattle.level == 5:
            if mybattle.defender.armydict['defender'] == 0:
                # giants only
                top = mybattle.reward//Army.costdict['giant']
                print(top)
                maxlogEV = 0
                giantnumber = 0
                for giantcount in range(top//2,top+1):
                    mybattle.attacker.armydict['giant'] = giantcount
                    battleresults = mybattle.battlelogEV(cash)
                    if battleresults[1] >= 0.0 and battleresults[0] > maxlogEV:
                        giantnumber = giantcount
                        maxlogEV = battleresults[0]
                print(maxlogEV)
                return Strategy(mybattle.name,giantnumber,"giant",maxlogEV)
            else:
                top = mybattle.defender.cost()//Army.costdict['battleship']
                maxlogEV = 0
                battleshipnumber = 0
                for battleshipcount in range(top//2,top):
                    mybattle.attacker.armydict['battleship'] = battleshipcount
                    battleresults = mybattle.battlelogEV(cash)
                    if battleresults[1] >= 0.0 and battleresults[0] > maxlogEV:
                        battleshipnumber = battleshipcount
                        maxlogEV = battleresults[0]
                print(maxlogEV)
                return Strategy(mybattle.name,battleshipnumber,"battleship",maxlogEV)
        return None