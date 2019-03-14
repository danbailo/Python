d = {"a":1,"b":1,"c":2}
# [["a","b"]:1,["c"]:2]

lst = []

for i in d:
    if i.values() == d.values():
        print(i)
        # lst = [i]



# print(d.values())

# print(lst)