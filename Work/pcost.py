# pcost.py
#
# Exercise 1.27
f = open('Data/portfolio.csv', 'rt')
header = next(f).split()
total_shares = 0
for line in f:
    line = line.replace('\n', '')
    row = line.split(',')
    print(row)
    total = int(row[1]) * float(row[2])
    total_shares = total_shares + total
       
print('Total number of shares: '+ str(total_shares))