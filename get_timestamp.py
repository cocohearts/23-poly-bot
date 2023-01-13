from re import S
from discord import getLastMessageGuild
from module.DiscordScraper import *
from time import sleep



def getLastTime():
    """
returns datetime of the last reap
"""
    discordscraper = DiscordScraper()
    for guild, channels in discordscraper.guilds.items():
        for channel in channels:
            lastdate = getLastMessageGuild(discordscraper, guild, channel)
            if lastdate == None:
                print("No internet, cannot fetch time")
                sleep(1200)
                return getLastTime()
            return lastdate

print(getLastTime())