import calendar

def find_leap(year):
    result = calendar.isleap(year)

    if result:
        print(f'{year} is leap year')
    else:
        print(f'{year} isn\'t leap year')

find_leap(1999)
find_leap(2000)
find_leap(2001)