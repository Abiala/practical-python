Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = open('foo.txt', 'rt')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    f = open('foo.txt', 'rt')
FileNotFoundError: [Errno 2] No such file or directory: 'foo.txt'
>>> g = open('bar.txt', 'wt')
>>> g.write('some text')
9
>>> g.close()
>>> with open(filename, 'rt') as file:
KeyboardInterrupt
>>> with open('bar.txt', 'rt') as file:
	file.read()

	
'some text'
>>> file.close()
>>> import os
>>> os.getcwd()
'C:\\Users\\Abiala Israel\\Documents\\practical-python\\practical-python\\Work'
>>> with open('Data/portfolio.csv', 'rt') as f:
	data = f.read()

	
>>> data
'name,shares,price\n"AA",100,32.20\n"IBM",50,91.10\n"CAT",150,83.44\n"MSFT",200,51.23\n"GE",95,40.37\n"MSFT",50,65.10\n"IBM",100,70.44\n'
>>> print(data)
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44

>>> f.close()
>>> with open('Data/portfolio.csv', 'rt') as f:
	for line in f:
		print(line, end='')

		
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>> f.close()
>>> f = open('Data/portfolio.csv', 'rt')
>>> headers = next(f)
>>> headers
'name,shares,price\n'
>>> for line in f:
	print(line, end='')

	
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>> f.close()
>>> f = open('Data/portfolio.csv', 'rt')
>>> headers = next(f).split(',')
>>> headers
['name', 'shares', 'price\n']
>>> for line n f:
	
SyntaxError: invalid syntax
>>> for line in f:
	row = line.split(',')
	print(row)

	
['"AA"', '100', '32.20\n']
['"IBM"', '50', '91.10\n']
['"CAT"', '150', '83.44\n']
['"MSFT"', '200', '51.23\n']
['"GE"', '95', '40.37\n']
['"MSFT"', '50', '65.10\n']
['"IBM"', '100', '70.44\n']
>>> f.close()
>>> int('32.20\n')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    int('32.20\n')
ValueError: invalid literal for int() with base 10: '32.20\n'
>>> '32.20\n'.rstrip()
'32.20'
>>> import gzip
>>> with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
	for line in f:
		print(line, end='')

		
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>> f.close()
>>> import csv
>>> f = open('Data/portfolio.csv')
>>> rows = csv.reader(f)
>>> next(rows)
['name', 'shares', 'price']
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> t = (row[0], int(row[1]), float(row[2]))
>>> t
('AA', 100, 32.2)
>>> cost = t[1] * t[2]
>>> cost
3220.0000000000005
>>> 
 RESTART: C:/Users/Abiala Israel/Documents/practical-python/practical-python/Work/tee.py 
Traceback (most recent call last):
  File "C:/Users/Abiala Israel/Documents/practical-python/practical-python/Work/tee.py", line 6, in <module>
    prices[row[0]] = float(row[1])
IndexError: list index out of range
>>> 
 RESTART: C:\Users\Abiala Israel\Documents\practical-python\practical-python\Work\report.py 
[('"AA"', 100, 32.2), ('"IBM"', 50, 91.1), ('"CAT"', 150, 83.44), ('"MSFT"', 200, 51.23), ('"GE"', 95, 40.37), ('"MSFT"', 50, 65.1), ('"IBM"', 100, 70.44)]
>>> portfolio
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    portfolio
NameError: name 'portfolio' is not defined
>>> 
 RESTART: C:\Users\Abiala Israel\Documents\practical-python\practical-python\Work\report.py 
[{'names': '"AA"', 'shares': 100, 'price': 32.2}, {'names': '"IBM"', 'shares': 50, 'price': 91.1}, {'names': '"CAT"', 'shares': 150, 'price': 83.44}, {'names': '"MSFT"', 'shares': 200, 'price': 51.23}, {'names': '"GE"', 'shares': 95, 'price': 40.37}, {'names': '"MSFT"', 'shares': 50, 'price': 65.1}, {'names': '"IBM"', 'shares': 100, 'price': 70.44}]
>>> portfolio
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    portfolio
NameError: name 'portfolio' is not defined
>>> prices = { }
>>> prices['IBM'] = 92.45
>>> prices['MSFT'] = 45.12
>>> prices
{'IBM': 92.45, 'MSFT': 45.12}
>>> data = { }
>>> import csv
>>> f = open('Data/prices.csv', 'r')
>>> rows = csv.reader(f)
>>> for row in rows:
	print(row)

	
['AA', '9.22']
['AXP', '24.85']
['BA', '44.85']
['BAC', '11.27']
['C', '3.72']
['CAT', '35.46']
['CVX', '66.67']
['DD', '28.47']
['DIS', '24.22']
['GE', '13.48']
['GM', '0.75']
['HD', '23.16']
['HPQ', '34.35']
['IBM', '106.28']
['INTC', '15.72']
['JNJ', '55.16']
['JPM', '36.90']
['KFT', '26.11']
['KO', '49.16']
['MCD', '58.99']
['MMM', '57.10']
['MRK', '27.58']
['MSFT', '20.89']
['PFE', '15.19']
['PG', '51.94']
['T', '24.79']
['UTX', '52.61']
['VZ', '29.26']
['WMT', '49.74']
['XOM', '69.35']
[]
>>> name = 'Eric'
>>> profession = 'comedian'
>>> affliation = 'Monty Python'
>>> message = ()
>>> message = (f"Hi {name}."  )
>>> message = (f"Hi {name}." f"You are a {profession}" f"You were in {affliation}." )
>>> message
'Hi Eric.You are a comedianYou were in Monty Python.'
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{name:>10s} {shares:>10d} {price:>10.2f}'
'       IBM        100      91.10'
>>> f'{name:<10s} {shares:<10d} {price:<10.2f}'
'IBM        100        91.10     '
>>> value = 42863.1
>>> print(value)
42863.1
>>> print(f'{value:0.4f}')
42863.1000
>>> print(f'{value:>16.2f}')
        42863.10
>>> print(f'{value:<16.2f}')
42863.10        
>>> print(f'{value:*>16,.2f}')
*******42,863.10
>>> 
