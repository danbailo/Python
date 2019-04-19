a = [0, 1, 2, 3, 4]
print(a,len(a))
b = a
a.append(a[:])
print(a, len(a))
a += "Py"
print(a, len(a))
del a

print(len(b), len(b[7:10]))