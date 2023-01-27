from getinfo import getBattles
from send_msg import main
from battles import *
from strategy import *
import datetime as dt


army1 = Army({'warrior': 73, 'archer': 90, 'rider': 0, 'defender': 58, 'mindbender': 86, 'knight': 73, 'catapult': 0, 'swordsman': 0, 'cloak': 90, 'giant': 0, 'boat': 68, 'ship': 0, 'battleship': 0})
army2 = Army({'warrior': 0, 'archer': 0, 'rider': 0, 'defender': 0, 'mindbender': 0, 'knight': 0, 'catapult': 0, 'swordsman': 0, 'cloak': 0, 'giant': 0, 'boat': 0, 'ship': 0, 'battleship': 63})

battle = Battle(army1,army2,1984,"battle",5)
print(army1.cost())
print(army2.cost())
# now = dt.datetime.now()
# print(battle.battlelogEV(2500))
# print(dt.datetime.now()-now)
def clock(number):
    army2.armydict['battleship'] = number
    now = dt.datetime.now()
    print(number,battle.battlelogEV(2500))
    print(dt.datetime.now()-now)

# for r in range(55,70):
#     clock(r)
now = dt.datetime.now()
print(dt.datetime.now())
strategy = Strategy.battleSolver(Battle(army1,Army(),1984,"name",5),2500)
print(
    strategy.battle.attacker.armydict,
    strategy.value
)
print(dt.datetime.now())
print(dt.datetime.now()-now)
# getBattles()
"""
knight(s) × 73
warrior(s) × 93
archer(s) × 90
defender(s) × 58
mindbender(s) × 86
cloak(s) × 90
boat(s) × 68
"""
# def fillout(self,unit,cash):
#     """fills with unit """
#     top = cash//Army.costdict[unit]
#     maxlogEV = 0
#     unitnumber = 0
#     for unitcount in range(0,top+1):
#         self.battle.attacker.armydict[unit] = unitcount
#         if unitnumber > 0 and unitcount > unitnumber + 3:
#             break
#         battleresults = self.battle.battlelogEV(cash)
#         if battleresults[1] >= 0.8 and battleresults[0] > maxlogEV:
#             unitnumber = unitcount
#             maxlogEV = battleresults[0]
#     self.battle.attacker.armydict[unit] = unitnumber
#     self.value = maxlogEV
#     return self

# # strategy2 = Strategy.battleSolver(Battle(army1,Army(),451,"name",5),1300)
# strategy2 = Strategy(Battle(army1,Army(),451,"name",5))
# strategy2 = fillout(strategy2,"battleship",1300)
# print(
#     strategy2.battle.attacker.armydict,
#     strategy2.value
# )