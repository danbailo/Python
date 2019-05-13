#https://www.datacamp.com/community/tutorials/json-data-python
#https://www.w3schools.com/python/python_json.asp

import pandas as pd

data = pd.read_json("https://api.github.com/users")
df = pd.DataFrame(data)

print(df)