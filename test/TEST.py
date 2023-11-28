# In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:
#
# Years divisible by 4 are leap years,
# but years divisible by 100 are not leap years,
# but years divisible by 400 are leap years.
# Tested years are in range 1600 ≤ year ≤ 4000.

year = 2100
if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
    print(year)
else:
    print('yt')


