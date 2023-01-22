from getinfo import getBattles
from send_msg import main
from battles import *
from strategy import *


army1 = Army({'warrior': 1, 'archer': 67, 'rider': 29, 'defender': 53, 'mindbender': 0, 'knight': 0, 'catapult': 0, 'swordsman': 0, 'cloak': 0, 'giant': 0, 'boat': 61, 'ship': 0, 'battleship': 0})
army2 = Army({'warrior': 0, 'archer': 0, 'rider': 0, 'defender': 0, 'mindbender': 0, 'knight': 0, 'catapult': 0, 'swordsman': 0, 'cloak': 0, 'giant': 0, 'boat': 0, 'ship': 0, 'battleship': 16})

battle = Battle(army1,army2,451,"battle",5)
print(army1.cost())
print(army2.cost())
print(battle.battlelogEV(1300))
strategy = Strategy.battleSolver(Battle(army1,Army(),451,"name",5),1300)
print(
    strategy.battle.attacker.armydict,
    strategy.value
)
# getBattles()
"""
warrior(s) × 1
rider(s) × 29
archer(s) × 67
defender(s) × 53
boat(s) × 61
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