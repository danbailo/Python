import calendar
import sys

def find_leap(year):
    result = calendar.isleap(year)

    if result:
        print(f'{year} is leap year')
    else:
        print(f'{year} isn\'t leap year')

find_leap(int(sys.argv[1]))
find_leap(int(sys.argv[2]))
find_leap(int(sys.argv[3]))
find_leap(int(sys.argv[4]))
