#!/usr/bin/python
# Extracts useful time series from the gsfc ice extent/area data.
# Must be given that data in stdin.

import sys
from timeseries import Timeseries
from datetime import datetime

ts = Timeseries()
first = True
for line in sys.stdin:
    if first:
        # Ignore header line
        first = False
        continue
    values = line.split()
    (year, month, value) = [int(values[x]) for x in (0, 1, 3)]
    d = datetime(year, month, 15)
    ts[d] = value/1e6

def year_to_bounds(y):
    s = "%04d-01-01 00:00" % (y,)
    e = "%04d-01-01 00:00" % (y+1,)
    return s, e

(start_year, end_year) = [x.year for x in ts.bounding_dates()]

print "Minimums"
for y in range(start_year, end_year+1):
    s, e = year_to_bounds(y)
    print "%04d %f" % (y, ts.min(s, e))

print "Maximums"
for y in range(start_year, end_year+1):
    s, e = year_to_bounds(y)
    print "%04d %f" % (y, ts.max(s, e))

print "Averages"
for y in range(start_year, end_year+1):
    s, e = year_to_bounds(y)
    print "%04d %f" % (y, ts.average(s, e))
