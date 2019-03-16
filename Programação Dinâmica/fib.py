import time
import timeit

n = 35

def fib(n):
	if n == 1 or n == 2:
		return 1
	return fib(n - 1) + fib(n - 2)

# fibonacci com PD
mem = [-1 for i in range(n)]
mem[0] = mem[1] = 1

def fib_pd(n):

	if mem[n - 1] != -1:
		return mem[n - 1]
	mem[n - 1] = fib_pd(n - 1) + fib_pd(n - 2)
	return mem[n - 1]


# print(fib_pd(n))
# print(fib(n))

# inicio = timeit.default_timer()
# fib(n)
# fim = timeit.default_timer()
# print ('duracao: %f' % (fim - inicio))

inicio = timeit.default_timer()
# print(fib_pd(n))
fib_pd(n)
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))