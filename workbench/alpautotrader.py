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

#First Party Library
from alpaca_trade_commands import *

#API Credentials
API_CRED = "data/keys.json"

api_cred = dataIO.load_json(API_CRED)
url = api_cred["Alpaca"]["paper"]["url"]
api_key = api_cred["Alpaca"]["paper"]["API_KEY_ID"]
api_secret = api_cred["Alpaca"]["paper"]["API_SECRET_KEY"]

#Default Command Prefix
bot = commands.Bot(command_prefix = "!")

print ("Discord Version " + discord.__version__)
bot_version = "0.0.1"
print ("Bot Version " + bot_version)

async def start():
    market_open = check_market_open(api_key, api_secret)
    if market_open is True:
        while market_open is True:
            await asyncio.sleep(15)
            check_status()
            market_open = check_market_open(api_key, api_secret)
    else:
        print("Market is Closed")
        
def check_status():
    profit_loss = check_stock_position()
    
    if profit_loss is None:
        buy_factor = 0.5
        run_buy(buy_factor)
    
    elif profit_loss >= 0.05:
        sell_factor = 1
        run_sell(sell_factor)

    elif profit_loss <= -.05:
        print("-----Loss Prevention-----")
        sell_factor = 0.15
        run_sell(sell_factor)
        buy_factor = 1
        run_buy(buy_factor)
        print("----------END------------")    
    return

def check_stock_position():
    position = stock_position(url, api_key, api_secret)

    return(position)

def run_buy(buy_factor):   
   buy(url, api_key, api_secret, buy_factor)
   return

def run_sell(sell_factor):
    sell(url, api_key, api_secret, sell_factor)
    return

asyncio.run(start())



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