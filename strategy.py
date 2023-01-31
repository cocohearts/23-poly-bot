from getinfo import *
from send_msg import main
from battles import *
from time import sleep
import random
import pause
from send_msg import main
import copy

class Strategy:
    def __init__(self,battle,logEV=0):
        self.battle = battle
        self.value = logEV
    
    def unitfillout(self,cash):
        """takes in a strategy prefilled with spellcasters, and fills with optimal giant/bs"""

        def fillout(self,unit,cash):
            """fills with unit """
            most = (self.battle.reward - self.battle.attacker.cost()) // Army.costdict[unit]
            top = most
            bottom = 0
            maxlogEV = 0
            unitnumber = 0
            # for unitcount in range(bottom,top+1):
            #     self.battle.attacker.armydict[unit] = unitcount
            #     if unitnumber > 0 and unitcount > unitnumber + 3:
            #         break
                
            #     battleresults = self.battle.battlelogEV(cash)
            #     if battleresults[1] >= 0.8 and battleresults[0] > maxlogEV:
            #         unitnumber = unitcount
            #         maxlogEV = battleresults[0]

            # first find 0
            while top > bottom + 1:
                midpoint = (top + bottom) // 2
                self.battle.attacker.armydict[unit] = midpoint
                if self.battle.battlelogEV(cash)[0] > 0:
                    top = midpoint
                else:
                    bottom = midpoint

            for unitcount in range(bottom,most+1):
                self.battle.attacker.armydict[unit] = unitcount
                if unitnumber > 0 and unitcount > unitnumber + 3:
                    break
                
                battleresults = self.battle.battlelogEV(cash)
                if battleresults[1] >= 0.8 and battleresults[0] > maxlogEV:
                    unitnumber = unitcount
                    maxlogEV = battleresults[0]

            self.battle.attacker.armydict[unit] = unitnumber
            self.value = maxlogEV
            return self
    
        if self.battle.defender.armydict['defender'] == 0 and self.battle.defender.armydict['mindbender'] == 0:
            return fillout(self,"giant",cash)

        else:
            return fillout(self,"battleship",cash)

    def battleSolver(mybattle,cash):
        print("solving",mybattle.name,"with",cash)
        if mybattle.defender.cost() < 2 * cash and mybattle.level in [5,10]:
            totalunits = 0
            for unit in mybattle.defender.armydict:
                totalunits += mybattle.defender.armydict[unit]
            # print(totalunits)
            mindbenderlessstrategy = Strategy(copy.deepcopy(mybattle))
            mindbenderstrategy = Strategy(copy.deepcopy(mybattle))

            mindbenderstrategy.battle.attacker.armydict["mindbender"] = totalunits
            
            mindbenderstrategy = mindbenderstrategy.unitfillout(cash)
            mindbenderlessstrategy = mindbenderlessstrategy.unitfillout(cash)

            if mindbenderstrategy.value > mindbenderlessstrategy.value:
                return mindbenderstrategy

            return mindbenderlessstrategy
        
        return Strategy(mybattle,0)

    def execute(self):
        for unit in self.battle.attacker.armydict:
            if self.battle.attacker.armydict[unit] != 0:
                main(" ".join(["..buy",unit,str(self.battle.attacker.armydict[unit])]),"token.txt")
        sleep(5)
        main(" ".join(["..battle",self.battle.name,"all"]),"token.txt")
        sleep(5)

        cash = getCash()
        
        waittime = datetime.datetime.now()
        waittime = waittime.replace(hour=16,minute=0,second=0)
        if waittime < datetime.datetime.now():
            waittime = waittime + datetime.timedelta(days=1)
        pause.until(waittime)

        return cash