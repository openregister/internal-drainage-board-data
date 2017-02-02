#!/usr/bin/env python3

import sys
import re

fields = ['urn', 'name', 'sector', 'subsector']

s = re.compile(r'\s\s+')
sep = '\t'

# third column is randomly a TLA/FLA
a = re.compile(r'[A-Z]{3,4}')

def pop(col):
    try:
        return col.pop(0)
    except IndexError:
        return ''

for line in sys.stdin:

    if line[0:5] == '     ':
        continue

    col = s.split(line.strip())

    if col[0] == 'URN':
        print(sep.join(fields))
        continue

    row = {}
    row['urn'] = pop(col)
    row['name'] = pop(col)
    row['sector'] = pop(col)

    if a.match(row['sector']) or row['sector'] == 'AbMAN':
        row['sector'] = pop(col)

    row['subsector'] = pop(col)

    if row['urn']:
        print(sep.join([row[field] for field in fields]))
