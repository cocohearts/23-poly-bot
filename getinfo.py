from discord import getLastMessageGuild
from module.DiscordScraper import *
from send_msg import main
from time import sleep
from battles import *

def getBattles():
    discordscraper = DiscordScraper()
    for guild, channels in discordscraper.guilds.items():
        for channel in channels:
            testdatapack = getLastMessageGuild(discordscraper, guild, channel)
            try:
                if testdatapack[0][0]['embeds'][0]['title'] == 'Found battles':
                    datapack = testdatapack
          
                    break
            except: pass

            while True:
                main("..scout","Number_0ne_token.txt")
                sleep(1)
                datapack = getLastMessageGuild(discordscraper, guild, channel)
                try:
                    if datapack[0][0]['embeds'][0]['title'] == 'Found battles':
                        break
                except:
                    continue
    data = datapack[0]

    rawbattles = data[0]['embeds'][0]['fields']
    battles = []
    for rawbattle in rawbattles:
        name = rawbattle['name'].split()[-1][:-4]
        
        levelstr = "Level "
        levelindex = rawbattle['name'].find(levelstr)
        level = 0
        if levelindex > 0:
            level = int(rawbattle['name'][levelindex+len(levelstr):].split()[0][:-1])

        block = rawbattle['value']
        reward = int(block.split()[1])
        locatorstr = "Estimated Units Present:\n"
        index = block.find(locatorstr)
        newblock = block[index+len(locatorstr):]
        opponent = Army()
        for line in newblock.split("\n"):
            splitline = line.split()
            unit = splitline[0][:-3]
            number = int(splitline[-1])
            opponent.armydict[unit] = number
        battles.append(Battle(opponent,Army(),reward,name,level))
    return battles

def getCash():
    discordscraper = DiscordScraper()
    for guild, channels in discordscraper.guilds.items():
        for channel in channels:
            while True:
                main("..player","token.txt")
                sleep(1)
                data = getLastMessageGuild(discordscraper, guild, channel)
                try:
                    if data[0][0]['embeds'][0]['title'] == 'fish4':
                        break
                except:
                    continue
    return int(data[0][0]['embeds'][0]['fields'][0]['value'].split()[0])


if __name__ == "__main__":
    # print(getCash())
    for battle in getBattles(400):
        print(battle.defender.armydict)
        if battle.level == 5:
            print(battle.name)