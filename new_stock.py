
import pandas_datareader as data
import pandas as pd
from datetime import datetime
import argparse 




parser = argparse.ArgumentParser(description= 'Calculate and Buy stock')
parser.add_argument('-t', '--stock', type=str, metavar='', help='Ticker for stock to buy' )
parser.add_argument('-s', '--start', type=str, const=1, default=str(datetime.now().strftime('%Y-%m-%d')), nargs='?', metavar='', help='Start date' )
parser.add_argument('-e','--end', type=str, const=1, default=str(datetime.now().strftime('%Y-%m-%d')), nargs='?', metavar='', help='end date' )
args = parser.parse_args()


def add_portfolio(stock,shares,total_stock,total_money):
    portfolio = []
    portfolio.extend([stock,shares,total_stock,total_money])
    return portfolio



def clean_data(start,end,stock_data, col):
    """This Function will take the stock data from yahoo finance and return the ADJ Close number

    Args:
        stock_data : This is the data for the given stock 
        col ([type]): The ADJ Close is a column so this will need to be provided too

    Returns:
        The ADJ Close for the stock
    """    
    weekdays = pd.date_range(start=start, end=end)
    clean_data = stock_data[col].reindex(weekdays)
    return clean_data.fillna(method='ffill')

def buy(stock, current):
    """This Function is calculate the purchase of a stock

    Args:
        stock : The ticker for given stock
        current : Current money before the purchase

    Returns:
        [type]: Will return portfolio after purchase of stock

    """   
    start = str(input("Enter buy date: "))
    end = start 
    stock_data = data.DataReader(stock, 'yahoo', start, end)
    
    adj_close = clean_data(start, end, stock_data, 'Adj Close')

    shares = int(input("How many shares you want to purchase "))
   
    total_stock = adj_close[0] * shares

    
    if total_stock < current:
        total_money = current - total_stock
        portfolio = add_portfolio(stock,shares,total_stock,total_money)
        return portfolio
        
       
    else:
        print("Not enough funds")
    
    
def sell (stock,portfolio):
    """This Function is calculate the sell of a stock

    Args:
        stock : The ticker for given stock
        portfolio : Current portfolio before the selling of a stock

    Returns:
        [type]: Will return portfolio after the selling of stock

    """   
    start = str(input("Enter sell date: "))
    end = start 
    stock_data = data.DataReader(stock, 'yahoo', start, end)
    adj_close = clean_data(start,end,stock_data, 'Adj Close')
  
    
    sell_shares = int(input("How many shares you want to sell "))
    if sell_shares > portfolio[1]:
        print("Not enough shares")
    else:
        remain_shares = portfolio[1] - sell_shares
        total_sell = adj_close[0] * sell_shares
        total = portfolio[3] + total_sell
        remain_stock = remain_shares * adj_close[0]
        if remain_stock == 0:
            stock = "None"
        portfolio = add_portfolio(stock,remain_shares,remain_stock,total)
        return portfolio
   


   



    

current = 1000
buy_stock = buy(args.stock, current)
sell_stock = sell(args.stock,buy_stock)
print(buy_stock)
print(sell_stock)


