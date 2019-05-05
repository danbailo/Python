import pandas as pd

s = pd.Series([3, -5, 7 ,4], index=['a', 'b', 'c', 'd'])

print(s)

print()

data = {
    'Country': ['Belgium', 'India', 'Brazil'],
    'Capital': ['Brussels', 'New Delhi', 'Brasília'],
    'Population': [11190846, 1303171035, 207847528]
    }

df = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])

print(df)