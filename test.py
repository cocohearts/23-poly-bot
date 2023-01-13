from getinfo import getBattles
from send_msg import main
from battles import *
from strategy import *


army1 = Army({'warrior': 17, 'archer': 0, 'rider': 0, 'defender': 24, 'mindbender': 0, 'knight': 0, 'catapult': 0, 'swordsman': 0, 'cloak': 0, 'giant': 0, 'boat': 0, 'ship': 23, 'battleship': 0})
army2 = Army({'warrior': 0, 'archer': 0, 'rider': 0, 'defender': 0, 'mindbender': 0, 'knight': 0, 'catapult': 0, 'swordsman': 0, 'cloak': 0, 'giant': 0, 'boat': 0, 'ship': 0, 'battleship': 6})

battle = Battle(army1,army2,155,"battle",5)
print(army1.cost())
print(battle.battlelogEV(500))
strategy = Strategy.battleSolver(Battle(army1,Army(),155,"name",5),500)
print(
    strategy.strategy,
    strategy.number,
    strategy.value
)