from getinfo import getBattles
from send_msg import main
from battles import *
from strategy import *
import datetime as dt


army1 = Army({'warrior': 28, 'archer': 0, 'rider': 0, 'defender': 89, 'mindbender': 41, 'knight': 0, 'catapult': 0, 'swordsman': 43, 'cloak': 91, 'giant': 65, 'boat': 0, 'ship': 0, 'battleship': 0})
army2 = Army({'warrior': 0, 'archer': 0, 'rider': 0, 'defender': 0, 'mindbender': 357, 'knight': 0, 'catapult': 0, 'swordsman': 0, 'cloak': 0, 'giant': 0, 'boat': 0, 'ship': 0, 'battleship': 0})

# battle = Battle(army1,army2,2217,"battle",5)
# print(army1.cost())
# print(army2.cost())
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
strategy = Strategy.battleSolver(Battle(army1,Army(),2217,"name",5),2500)
print(
    strategy.battle.attacker.armydict,
    strategy.value
)
print(dt.datetime.now())
print(dt.datetime.now()-now)
# getBattles()
"""
warrior(s) × 28
defender(s) × 89
swordsman(s) × 43
giant(s) × 65
mindbender(s) × 41
cloak(s) × 91
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