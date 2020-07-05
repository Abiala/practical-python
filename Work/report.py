# report.py
#
# Exercise 2.4
import csv
def read_portfolio(filename):
    '''Read a stock portfolio file into a list of dictionaries
       with keys names, shares and prices. 
    '''
    portfolio = []
    with open(filename) as f:
        k = csv.reader(f)
        next(k)
        for line in f:
            row = line.split(',')
            stock = {'names': row[0] , 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(stock)
    print(portfolio)
portfolio = read_portfolio('Data/portfolio.csv')   

def read_prices(filename):
    '''Read a price csv file and store the data with names as key
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
        print(prices)
prices = read_prices('Data/prices.csv')

def make_report(portfolio, prices):
    '''Make a list of tuples(names, shares, price, change) given a portfolio list
       and price dictionary
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['names']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows


    