# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    f = open(filename, 'rt')
    header = next(f).split()
    total_shares = 0
    for rowno, row in enumerate(f, start=1):
        try:
            row = row.replace('\n', '')
            row = row.split(',')
            print(row)
            total = int(row[1]) * float(row[2])
            total_shares = total_shares + total
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')

    print('Total number of shares: '+ str(total_shares))
portfolio_cost('Data/missing.csv')