import math
import random

from sympy import false

def diceroll(n):
    return random.randint(1,n)

class unitProfile:
    def __init__(self,iterations,size,flat,knight=False):
        self.iterations = iterations
        self.size = size
        self.flat = flat
        self.knight = knight
    
    def roll(self):
        roll = self.flat
        if self.knight:
            while True:
                newroll = diceroll(12)
                roll += newroll
                if newroll < 10:
                    break
        else:
            for iteration in range(self.iterations):
                roll += diceroll(self.size)
        
        return roll

class unitRoll:
    def __init__(self,roll):
        self.roll = roll
        self.debuffed = False

class Army:
    rolldict = {
            "warrior" : unitProfile(1,3,0),
            "archer" : unitProfile(1,5,0),
            "rider" : unitProfile(1,4,1),
            "defender" : unitProfile(0,0,0),
            "mindbender" : unitProfile(0,0,0),
            "knight" : unitProfile(0,0,0,True),
            "catapult" : unitProfile(2,10,0),
            "swordsman" : unitProfile(2,4,2),
            "cloak" : unitProfile(3,3,0),
            "giant" : unitProfile(6,12,11),
            "boat" : unitProfile(1,2,0),
            "ship" : unitProfile(2,4,0),
            "battleship" : unitProfile(4,12,4)
        }

    costdict = {
            "warrior" : 2,
            "archer" : 3,
            "rider" : 3,
            "defender" : 3,
            "mindbender" : 5,
            "knight" : 10,
            "catapult" : 8,
            "swordsman" : 5,
            "cloak" : 8,
            "giant" : 30,
            "boat" : 2,
            "ship" : 5,
            "battleship" : 20
        }

    meleeunits = [
        "warrior",
        "rider",
        "knight",
        "swordsman",
        "giant"
    ]

    def __init__(self, armydict = None):
        if not armydict:
            self.armydict = {
                "warrior" : 0,
                "archer" : 0,
                "rider" : 0,
                "defender" : 0,
                "mindbender" : 0,
                "knight" : 0,
                "catapult" : 0,
                "swordsman" : 0,
                "cloak" : 0,
                "giant" : 0,
                "boat" : 0,
                "ship" : 0,
                "battleship" : 0
            }
        else:
            self.armydict = armydict
        self.rangedrolls = []
        self.meleerolls = []
        self.rolls = []
        self.mindbender = 0

    def roll(self):
        self.rangedrolls = []
        self.meleerolls = []

        for unit in self.armydict:
            for iteration in range(self.armydict[unit]):
                newroll = self.rolldict[unit].roll()
                if unit in self.meleeunits:
                    self.meleerolls.append(unitRoll(newroll))
                else:
                    self.rangedrolls.append(unitRoll(newroll))

    def cost(self):
        armycost = 0
        for unit in self.armydict:
            armycost += self.armydict[unit] * self.costdict[unit]
        return armycost
    
    def debuff(self,opponent):
        """debuff opponent"""
        def unitdebuff(opponent,factor,size,ranged):
            rangedundebuffed = []
            meleeundebuffed = []
            for unit in opponent.rangedrolls:
                if not unit.debuffed:
                    rangedundebuffed.append(unit)
            
            for unit in opponent.meleerolls:
                if not unit.debuffed:
                    meleeundebuffed.append(unit)

            debuffed = random.sample(rangedundebuffed + meleeundebuffed,min(size,len(rangedundebuffed) + len(meleeundebuffed)))

            if not ranged:
                for unit in debuffed:
                    if unit in opponent.rangedrolls:
                        debuffed.remove(unit)
            
            diff = 0
            for unitroll in debuffed:
                newval = math.floor(unitroll.roll*factor)
                diff += unitroll.roll - newval
                unitroll.roll = newval
                unitroll.debuffed = True
            return diff

        self.mindbender = unitdebuff(opponent,0.5,self.armydict["mindbender"],False)
        unitdebuff(opponent,1/3,3*self.armydict["cloak"],True)
        unitdebuff(opponent,1/3,self.armydict["defender"],False)

class Battle:
    def __init__(self, defender, attacker, reward, name, level=0):
        self.defender = defender
        self.attacker = attacker
        self.reward = reward
        self.name = name
        self.level = level
    
    def battle(self):
        self.defender.roll()
        self.attacker.roll()
        self.defender.debuff(self.attacker)
        self.attacker.debuff(self.defender)
        defenderscore = self.defender.mindbender
        attackerscore = self.attacker.mindbender
        for defenderroll in self.defender.meleerolls + self.defender.rangedrolls:
            defenderscore += defenderroll.roll
        
        for attackerroll in self.attacker.meleerolls + self.attacker.rangedrolls:
            attackerscore += attackerroll.roll
        if attackerscore < defenderscore:
            pass
        return (attackerscore >= defenderscore)

    def battlelogEV(self,cash):
        runs = 1000
        wins = 0
        for run in range(runs):
            wins += self.battle()
        probability = wins/runs
        try:
            logwin = math.log((cash+self.reward-self.attacker.cost())/cash)
            logloss = math.log((cash-self.attacker.cost())/cash)
        except:
            return (float('-inf'),0)
        logEV = logwin * probability + logloss * (1-probability)

        return (logEV, probability)