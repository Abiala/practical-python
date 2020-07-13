# fileparse.py
#
# Exercise 3.3

import csv 

def parse_csv(filename, types = [str, float]):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        prices = []
        for row in rows:
            if not row:     # Skip rows with no data
                continue
            record = [ func(val) for func, val in zip(types, row) ]
            record = tuple(record)
            prices.append(record)

    return prices

prices = parse_csv('Data/prices.csv')
    
