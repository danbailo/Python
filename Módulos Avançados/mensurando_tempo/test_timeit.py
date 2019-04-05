def f1():
    return list(range(10))

def f2():
    return [x for x in range(10)]

def f3(n):
    lst = []
    i = 0
    while i < n:
        lst.append(i)
        i += 1
    return lst

from timeit import timeit

v1 = timeit('f3(1)', 'from __main__ import f3', number=100)
v2 = timeit('f3(100)', 'from __main__ import f3', number=100)
v3 = timeit('f3(1000)', 'from __main__ import f3', number=100)

print(v1, v2, v3)

def fib(n):
	if n==0 or n==1:
		return 1
	return fib(n-1)+fib(n-2)

inicio = timeit.default_timer()
fib(40)
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))