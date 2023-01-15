from getinfo import getBattles
from send_msg import main
from battles import *
from strategy import *


army1 = Army({'warrior': 75, 'archer': 75, 'rider': 0, 'defender': 0, 'mindbender': 0, 'knight': 58, 'catapult': 55, 'swordsman': 91, 'cloak': 0, 'giant': 0, 'boat': 32, 'ship': 0, 'battleship': 0})
army2 = Army({'warrior': 0, 'archer': 0, 'rider': 0, 'defender': 0, 'mindbender': 170, 'knight': 0, 'catapult': 0, 'swordsman': 0, 'cloak': 0, 'giant': 25, 'boat': 0, 'ship': 0, 'battleship': 0})

battle = Battle(army1,army2,1416,"battle",5)
print(army1.cost())
print(army2.cost())
print(battle.battlelogEV(1800))
# strategy = Strategy.battleSolver(Battle(army1,Army(),800,"name",5),3000)
# print(
#     strategy.battle.attacker.armydict,
#     strategy.value
# )
# getBattles()