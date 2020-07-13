# fileparse.py
#
# Exercise 3.3

import csv 

def parse_csv(filename, types = [str, int, float]):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        #Read the file headers
        headers = next(rows)
        records = []
        for row in rows:
            if not row:     # Skip rows with no data
                continue
            row = [func(val) for func, val in zip(types, row)]
            record = dict(zip(headers, row))
            records.append(record)

    return records

portfolio = parse_csv('Data/portfolio.csv')
    
