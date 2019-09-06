'''
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
'''

import calendar
import time
import datetime
print("Current date and time:" , datetime.datetime.now())
print("Current day and time:" , time.asctime(time.localtime(time.time())))
print("Year:" , datetime.date.today().strftime("%Y"))
print("Month:" , datetime.date.today().strftime("%B"))
print("Week:" , datetime.date.today().strftime("%W"))
print("Weekday:" , datetime.date.today().strftime("%w"))
print("Day of Year:" , datetime.date.today().strftime("%j"))
print("Day of Month:" , datetime.date.today().strftime("%d"))
print("Day of week:" , datetime.date.today().strftime("%A"))
