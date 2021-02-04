#Third party & System resources
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Client
import asyncio
import json
from utils.dataIO import dataIO
import os
from copy import deepcopy
from Pairs_Trading_Algo_Example import pairs_trading_algo
import threading

#API Credentials
API_CRED = "data/keys.json"

#Default Command Prefix
bot = commands.Bot(command_prefix = "!")

print ("Discord Version " + discord.__version__)
bot_version = "0.0.1"
print ("Bot Version " + bot_version)

def run_paper():
   api_cred = dataIO.load_json(API_CRED)
   url = api_cred["Alpaca"]["paper"]["url"]
   api_key = api_cred["Alpaca"]["paper"]["API_KEY_ID"]
   api_secret = api_cred["Alpaca"]["paper"]["API_SECRET_KEY"]
   
   active_check = pairs_trading_algo(url, api_key, api_secret)

   return active_check

def auto_run():
    is_active = True
    if is_active is True:
        execute = threading.Timer(1.0,auto_run)
        execute.start()
        is_active = run_paper()
    
    else:
        execute.wait()
        execute.cancel()

auto_run()


#Boot Checks for Bot
#@bot.event
#async def on_ready():
#    online = "Auto Trader Online"
#    print("Will operate as " + bot.user.name)
#    print("With the ID of: " + bot.user.id)

#    print("Gathering Credentials...")
#    check_trainer_directory()
#    check_trainer_log()
#    print("Checking for Tournament Log...")
#    check_tournament_directory()
#    check_tournament_log()

#    print(online)