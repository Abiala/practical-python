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
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            record = dict(zip(header, row))
            stock = {'name': record['name'] , 'shares': int(record['shares']), 'price': float(record['price'])}
            portfolio.append(stock)
    return(portfolio)
   

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
        return(prices)


def  make_report(portfolio, prices):
    '''Make a list of tuples(names, shares, price, change) given a portfolio list
       and price dictionary
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

def print_report(report):
    '''
    Print a formatted table from a list of (names, shares, price, change) tuples.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfoliofile, pricefile):
    '''
    Read the portfolio and price csv files.
    '''
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    #Make a report.

    report = make_report(portfolio, prices)
    
    #Output the report

    print_report(report)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')