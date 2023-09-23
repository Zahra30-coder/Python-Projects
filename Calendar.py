import calendar
import datetime
import time

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2023,2))
#printing out a single month

print(calendar.monthcalendar(2024,3))
#printing out the month in a different format

print(calendar.calendar(2023))

day_of_the_week = calendar.weekday(2023, 5, 3 )
print(day_of_the_week)

is_leap = calendar.isleap(2020)
print(is_leap)

how_many_leap_days = calendar.leapdays(2000, 2005)
print(how_many_leap_days)

#2000 and 2004 are both leap years
#on entering 2004 its exclusive, so we have to enter 2005
