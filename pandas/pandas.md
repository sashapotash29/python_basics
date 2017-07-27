# Pandas Notes

### Pandas-Datareader

- Used for accessing data.
- One of the applications of the datareader would be for accessing information from a URL.

```
start = datetime.date(2016,1,1)
end = datetime.date.today()


stock_prices = web.DataReader("TWTR", "google", start, end)
```
- You provide a symbol, the search engine, and the start and ending dates as date objects and you will be returned the prices that are in that range of dates.

### Accessing Sections of Data

```
closingPricesSlice = stock_prices.Close

closingPricesSlice = stock_prices['Close']
```

### Adding new columns
```
stock_prices["New"] = 0

stock_prices["Range"] = abs(stock_prices['Open'] - stock_prices['Close'])
```

### Simple Graph with matplotlib

```
y = [1,2,3,4,5]
x = [1,2,3,4,5]

plt.plot(x,y)
plt.show() 

```

### Graphs using DataFrame object
```
stock_prices[["Close",'High']].plot()
plt.show()
```

### Moving Average Example

```
stock_prices['MA'] = stock_prices['Close'].rolling(window=10).mean()
print(stock_prices)
```

- window variable implies the amount of periods.

### Create Datafram object from Python objects

```
stocks = ["IBM", "APPLE", "TWITTER"]
prices = [115, 119, 19]

portfolio = list(zip(stocks,prices))

portfolioDf = pd.DataFrame(data=portfolio, columns=['Stocks', 'Prices'])
print(portfolioDf)
```

#### Adding another column to Dataframe

- From a list:
```
porfolioDf["NewColumn"] = ["New", "Old", "Better"]
```
