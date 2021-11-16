#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 16:22:41 2021

@author: jamestang1
"""

# importing packages
from IPython.display import HTML
import pandas as pd 
import numpy as np
import os 
from scipy import stats
from scipy.stats import chi2_contingency
from collections import defaultdict
from scipy.stats import norm, inom, beta
import re 
# # name: Siwei Tang Email: tangsw@umich.edu
# # Q0
# ## Time series/ data functionality
#
# The Python world has a number of available representation of dates, times, deltas, and timespans. Whiles the times series tools provided by Pandas tend to be the most useful for data science applications, it's helpful to see their relationsip to other packages used in Python.
#
# ## Native Python dates and times: `datetime` and `dateutil`
#
# Pythonn's baseic objects for working with dates and times reside in the built-in `dateime` module. Along with the third-party `dateutil` module, you can use it to quickly perform a host of useful functionalities on dates and time. 

# - build a date using the `datetime` type

from datetime import datetime
datetime(year = 2021, month=10, day=20)

# - using dateutil module to parse dates from a variety of strng formats

from dateutil import parser
date = parser.parse("20th of October, 2021")
date 

# - Once you have a `datetime` object, you can do things like printing the day of the week:

date.strftime('%A')

# In the final line, `%A` is part of the [strfyime section](https://docs.python.org/3/library/datetime.html) od Python's [datetime documentation]()

# ## Typed arrays of times: Numpy's `datatime64`
# - The `datatime64` dtype encoded dates as 64-bit inegers, and thus allows arrays of dates to be represented very compactly. The `datatime64` requires a very specific input format:

date =np.array('2021-10-20', dtype=np.datetime64)
date

# - Once we have this date formated, however, we can quickly do vectorized operations on it

date + np.arange(12)

# - One detail of the `datetime64` and `timedelta64` object is that they are build on a fundamental time unit. Because the `datetime64` object is limited to 64-bit precision, the range of encodable times is $2^{64}$ times this fundamental unit. In other words, `datetime64` imposes a trade-off between **time resolution** and **maximum time span**.

# ## Dates and times in pandas: best of both worlds
# Pandas builds upon all the tools just discussed to provide a `Timestamp` object, which combines the ease-of-use of `datetime` and `dateutil` with the efficient storage and vectorized interface of `numpy.datetime64`. From a group of these `Timestamp` objects, Pandas can construct a `DatetimeIndex` that can be used to index data in a `Series` or `DataFrame`.

date = pd.to_datetime('20th of October, 2021')
date

date.strftime('%A')

# - we can do Numpy-style vectorized operations directly on this same object:

date + pd.to_timedelta(np.arange(12),'D')

# ## Pandas Time Series Data Structures
# - for time stamps, Pandas provides the `Timestamp` type. As mentioned before, it is essentially a replacement for Python's native `datetime`, but is based on the more efficient `numpy.datetime64` date type. The associated Index structure is `DatetimeIndex`. 
# - for time Periods, Pandas provides the `Period` type. This encodes a fixed-frequency interval based on `numpy.datetime64`. The associated index structure is `PeriodIndex`.
# - For time deltas or durations, Pandas provides the `Timedelta` type. `Timedelta` is a more efficient replacement for Python's native `datetime.timedelta` type, and is based on `numpy.timedelta64`. The assocaited index structure is `TimedeltaIndex`.
#
# Passing a single date to `pd.to_datetime()` yields a `Timestamp`; passing a series of dates by default yields a `DatetimeIndex`:

dates = pd.to_datetime([datetime(2021,10,20),
                        '21st of October, 2021',
                        '2021-Oct-22',
                       '10-23-2021',
                       '20211024'])
dates

# - Any `DatetimeIndex` can be converted to a `PeriodIndex` with the `to_period()` function with the addition of a frequency code; here we use `'D'` to indicate daily frequency.

dates.to_period('D')

# - A `TimedeltaIndex` is created, for example, when a date is subtracted from another:

dates - dates[0]

# ## Regular Sequences: `pd.date_range()`

# - `pd.date_range()` for timestamsps, `pd.period_range()` for periods, and `pd.timedelta_range()` for time deltas. This is similar to Python's `range()` or `np.arange()`.

pd.date_range('2021-09-11','2021-10-21')

# - Alternatively, the date range can be specified not with a start and end point, but with a startpoint and a number of periods
# - The spacing can be modified by altering the `freq` argument, which defaults to `D`.

print(pd.date_range('2021-09-11',periods=10))
print(pd.date_range('2021-09-11', periods = 10, freq = 'H'))

# - To create regular sequencs of `Period` or `Timedelta` values, the very similar `pd.period_range()` and `pd.timedelta_range()` functions are useful. Here are some monthly periods:

pd.period_range('2021-09',periods = 10, freq='M')

# - A sequence of durations increasing by an hour:

pd.timedelta_range(0,periods=30, freq='H')
