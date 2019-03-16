from collections import defaultdict
#Using list as the default_factory, it is easy to group a sequence of key-value pairs 
#into a dictionary of lists:

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

print(s)
d = defaultdict(list)
print(d)

for k,v in s:
    d[k].append(v)

print(d.items())

for k in d.values():
    print(k)