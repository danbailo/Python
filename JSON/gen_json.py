import json

data = {'key'+str(i):i for i in range(10)}

print(data)

with open("result.json","w") as f:
    f.write(json.dumps(data,indent=4))