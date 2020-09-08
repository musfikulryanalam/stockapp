
import pandas_datareader as data
import pandas as pd
from datetime import datetime

Start = '2020-08-03'
end =  '2020-08-03'

stock = "AMZN"

def clean_data(stock_data, col):
    weekdays = pd.date_range(start=Start, end=end)
    clean_data = stock_data[col].reindex(weekdays)
    return clean_data.fillna(method='ffill')

def get_data(ticker, current):
    stock_data = data.DataReader(stock, 'yahoo', Start, end)
    
    adj_close = clean_data(stock_data, 'Adj Close')

    shares = int(input("How many shares you want to purchase "))
   
    total_stock = adj_close[0] * shares

    
    if total_stock < current:
        total = current - total_stock
        return total
    else:
        print("Not enough funds")
    
    


current = 10000
stock_data = get_data(stock,current)
print(stock_data)

