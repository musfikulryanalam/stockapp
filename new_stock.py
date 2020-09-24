
import pandas_datareader as data
import pandas as pd
from datetime import datetime
import argparse 

start = '2020-08-03'
end =  '2020-08-03'

stock = "AMZN"

parser = argparse.ArgumentParser(description= 'Calculate and Buy stock')
parser.add_argument('-t', '--stock', type=str, metavar='', help='Ticker for stock to buy' )
parser.add_argument('-s', '--start', type=str, const=1, default=str(datetime.now().strftime('%Y-%m-%d')), nargs='?', metavar='', help='Start date' )
parser.add_argument('-e','--end', type=str, const=1, default=str(datetime.now().strftime('%Y-%m-%d')), nargs='?', metavar='', help='end date' )
args = parser.parse_args()


def clean_data(stock_data, col):
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

def get_data(stock, start, end, current):
    """This Function is to return the stock and calculate the shares and current balance

    Args:
        stock : The ticker for given stock
        start : Start date of purchase
        end   : End date of purchase
        current : Current money before the purchase

    Returns:
        [type]: Will return total balance after purchase of stock
    """    
    stock_data = data.DataReader(stock, 'yahoo', start, end)
    
    adj_close = clean_data(stock_data, 'Adj Close')

    shares = int(input("How many shares you want to purchase "))
   
    total_stock = adj_close[0] * shares

    
    if total_stock < current:
        total = current - total_stock
        return total
    else:
        print("Not enough funds")
    
    


current = 10000
stock_data = get_data(args.stock,args.start, args.end, current)
print(stock_data)

