# This is just my psudo code for the buy feature. Not the full logic but my idea of what I want to do

# First  Need to create a method to clean up the data, since yahoo finance gives the high,low, and adjusted close. The data is a bit messy.
# Will need to clean up the data to just give the Adjusted Close

def clean_data(stock_data,col):
    day = pd.date_range(start=Start_DATE, end = End_DATE)
    clean_data = stock_data[col].reindex(day)
    return clean_data.fillna(method='ffill')

# Now that there is a method to clean data, will need to use that and make the buy feature
# This is will caluclate the price of stock times shares and subtract from the current balance

def buy_stock(ticker,current):
    start = Date.Now()
    end   = Date.Now()

    stock = data.Data.DataReader( ticker,
                                  'yahoo',
                                   start,
                                   end    )
    adjusted_close = clean_data(stock, 'Adj Close')
    shares = input("How many Shares")
    total_shares = adjusted_close * shares
    if total_shares > current:
        print("Not enough money")
    
    total = current - total_shares
    return total


