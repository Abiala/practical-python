# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    f = open(filename, 'rt')
    header = next(f)
    print(header)
    rows = next(f)
    total_cost = 0
    for rowno, row in enumerate(rows, start=1):
        record = dict(zip(header, rows))
        try:
           nshares = int(record['shares'])
           price = float(record['price'])
           total_cost += nshares * price
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')

    print('Total number of shares: '+ str(total_cost))
portfolio_cost('Data/portfoliodate.csv')