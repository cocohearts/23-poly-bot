from getinfo import getBattles
from send_msg import main
from battles import *
from strategy import *


army1 = Army({'warrior': 36, 'archer': 0, 'rider': 68, 'defender': 53, 'mindbender': 0, 'knight': 52, 'catapult': 0, 'swordsman': 0, 'cloak': 0, 'giant': 0, 'boat': 70, 'ship': 0, 'battleship': 0})
army2 = Army({'warrior': 0, 'archer': 0, 'rider': 0, 'defender': 0, 'mindbender': 0, 'knight': 0, 'catapult': 0, 'swordsman': 0, 'cloak': 0, 'giant': 0, 'boat': 0, 'ship': 0, 'battleship': 38})

battle = Battle(army1,army2,854,"battle",5)
print(army1.cost())
print(army2.cost())
print(battle.battlelogEV(779))
# strategy = Strategy.battleSolver(Battle(army1,Army(),800,"name",5),3000)
# print(
#     strategy.battle.attacker.armydict,
#     strategy.value
# )
# getBattles()