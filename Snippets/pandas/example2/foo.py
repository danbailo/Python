import pandas as pd
import json

list1 = ['India', 'New Delhi', 'USA',
         'Washington, D.C.', 'China',
         'Beijing', 'Russia', 'Moscow']

# print(list1[0::2])

df = pd.DataFrame()

# print(df)

#creating two columns
df['Country'] = list1[0::2]
df['Capital'] = list1[1::2]

print(df)

#converting to excel
df.to_excel('result.xlsx', index=False)

df.to_json('result1.json')

with open('result2.json','w') as result:
    result.write(json.dumps(df.to_dict(), indent=4))