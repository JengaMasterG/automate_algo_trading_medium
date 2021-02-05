import os
import alpaca_trade_api as tradeapi
import pandas as pd
from alpaca_trade_api import rest

def check_market_open(api_key, api_secret):
    key_id = api_key
    secret = api_secret
        
    #Insert API Credentials 
    api = tradeapi.REST(key_id, secret, api_version='v2') # or use ENV Vars shown below
    
    #Check if the Market is Open or Closed
    clock = api.get_clock()

    if clock.is_open is True:
        return True
    
    else:
        return False


def buy(url, api_key, api_secret, buy_factor):
    api_url = url
    key_id = api_key
    secret = api_secret        
    
    #Specify the trading environment (Either Live or Paper)
    os.environ["APCA_API_BASE_URL"] = api_url
    
    #Insert API Credentials 
    api = tradeapi.REST(key_id, secret, api_version='v2') # or use ENV Vars shown below
    account = api.get_account()      
    
    #Designate the stock to use
    stock = 'AAPL'

    #------------Buy Stocks at Market-------------------
    
    #Obtain Buying Power
    buy_power = float(account.buying_power)
    
    #Obtain Price of Stock
    last_trade = api.get_last_trade(stock).price

    #Calculate no of shares to buy
    number_of_shares = int(float(buy_power//last_trade)*float(buy_factor))
    
    print("Buying ", number_of_shares, " shares of " + stock)

    #Submit Order
    api.submit_order(symbol = stock,qty = number_of_shares,side = 'buy',type = 'market',time_in_force ='day')

    print("Your order of " + stock + " stock has been submitted!")

    return
    
def sell(url, api_key, api_secret, short_factor):
    api_url = url
    key_id = api_key
    secret = api_secret        
    
    #Specify the trading environment (Either Live or Paper)
    os.environ["APCA_API_BASE_URL"] = api_url
    
    #Insert API Credentials 
    api = tradeapi.REST(key_id, secret, api_version='v2') # or use ENV Vars shown below
    
    #Designate the stock to use
    stock = 'AAPL'

    #------------Sell Stocks at Market-------------------

    #Grab total number of shares owned
    number_of_shares = int(float(api.get_position(stock).qty)*float(short_factor))

    print("Selling ", number_of_shares, " shares")
    
    #Submit Order
    api.submit_order(symbol = stock,qty = number_of_shares,side = 'sell',type = 'market',time_in_force ='day')
    
    print("Your sale for " + stock + " stock has been submitted!")

    return

#def buy_cover(url, api_key, api_secret):
#     api_url = url
#     key_id = api_key
#     secret = api_secret        
    
#     #Specify the trading environment (Either Live or Paper)
#     os.environ["APCA_API_BASE_URL"] = api_url
    
#     #Insert API Credentials 
#     api = tradeapi.REST(key_id, secret, api_version='v2') # or use ENV Vars shown below
#     account = api.get_account()

#     #Designate the stock to use
#     stock = 'AAPL'

#     #------------Sell Stocks at Market-------------------

#     #Obtain Buying Power
#     buy_power = float(account.buying_power)
    
#     #Obtain Price of Stock
#     last_trade = api.get_last_trade(stock).price

#     #Calculate no of shares to buy
#     number_of_shares = (int(buy_power//last_trade))-1

#     print(number_of_shares)

#     #Submit Order
#     api.submit_order(symbol = stock,qty = number_of_shares,side = 'buy',type = 'market',time_in_force ='day')
    
#     print("Taking a short position in" + stock + "!")

#     return

    
def stock_position(url, api_key, api_secret):
    api_url = url
    key_id = api_key
    secret = api_secret
    
    #Specify the trading environment (Either Live or Paper)
    os.environ["APCA_API_BASE_URL"] = api_url
    #Insert API Credentials 
    api = tradeapi.REST(key_id, secret, api_version='v2') # or use ENV Vars shown below

    stock = 'AAPL'

    print("Checking stock position...")

    try:
        current_position = api.get_position(stock).avg_entry_price
    
    except rest.APIError as http_error:
        http_error = None
        print("No stock taken out (HTTP Error 404 handled)")
        return http_error
    
    else:
        unrealized_profit_loss = float(api.get_position(stock).unrealized_plpc)*100
        print("\rAvg Entry Price: " + str(current_position), " % Profit/Loss: " + str(unrealized_profit_loss))
        return (unrealized_profit_loss)

#def buy_power():
#    print(float(account.buying_power))

