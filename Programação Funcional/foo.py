def fat(n):
    if (n==0):
        return 1
    return (n*fat(n-1))

print(fat(3))

fat_ = lambda n: (n*fat_(n-1)) if n > 1 else 1

print(fat_(5))

lst = [1, 2, 3]

m = map(lambda x : x**2, lst)

print (list(m))

import functools

print(functools.reduce(lambda x,y : x+y,[1, 2, 3, 4]))

f = filter(lambda x : x%2==0, range(11))

print(list(f))