#lambda
def fahrenheit(t):
    return (9/5)*t+32

temp = [9, 22, 40, 90, 120]

temp_f = []

for t in temp:
    temp_f += [fahrenheit(t)]
print(temp_f)

print(list(map(fahrenheit,temp)))

print(list(map(lambda t:(9/5)*t+32, temp)))