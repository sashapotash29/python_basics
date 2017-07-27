import pandas as pd
import pandas_datareader as web
import datetime
import matplotlib.pyplot as plt

start = datetime.date(2016,1,1)
end = datetime.date.today()


stock_prices = web.DataReader("TWTR", "google", start, end)

# # Provides the top "n" rows in your DataFrame
# print(stock_prices.head(5))


# # Select a specific column (Slices the dataframe object)
# print(stock_prices.Close)
# # Identical version is:
# print(stock_prices['Close'])

# # ADDING COLUMNS
# stock_prices["Range"] = abs(stock_prices['Open'] - stock_prices['Close'])
# print(stock_prices)

# # CREATING GRAPHS
# y = [1,2,3,4,5]
# x = [1,2,3,4,5]

# plt.plot(x,y)
# plt.show() 

# stock_prices[["Close",'High']].plot()
# plt.show()

# # MOVING AVERAGE EXAMPLE
# stock_prices['MA'] = stock_prices['Close'].rolling(window=10).mean()
# print(stock_prices)

# # CREATE DATAFRAME OBJECT
# stocks = ["IBM", "APPLE", "TWITTER"]
# prices = [115, 119, 19]

# portfolio = list(zip(stocks,prices))

# portfolioDf = pd.DataFrame(data=portfolio, columns=['Stocks', 'Prices'])
# print(portfolioDf)

# # ADDING ANOTHER COLUMN TO DATAFRAME
# porfolioDf["NewColumn"] = ["New", "Old", "Better"]






