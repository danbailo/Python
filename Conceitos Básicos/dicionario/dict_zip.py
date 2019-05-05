key = ['a','b','c','d']
value = [2,5,1,9]

print(zip(key,value))

d = dict(zip(key,value))
print(d)

l = list(zip(key,value))
print(l)

print(dict(l))