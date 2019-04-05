import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from timeit import timeit

def fib(n):
	if n==1 or n==2:
		return 1
	return fib(n-1)+fib(n-2)

if __name__ == "__main__":
	t0 = timeit('fib(1)', 'from __main__ import fib', number=1)
	t1 = timeit('fib(3)', 'from __main__ import fib', number=1)
	t2 = timeit('fib(6)', 'from __main__ import fib', number=1)
	t3 = timeit('fib(9)', 'from __main__ import fib', number=1)
	t4 = timeit('fib(12)', 'from __main__ import fib', number=1)
	t5 = timeit('fib(15)', 'from __main__ import fib', number=1)
	t6 = timeit('fib(18)', 'from __main__ import fib', number=1)
	t7 = timeit('fib(21)', 'from __main__ import fib', number=1)
	t8 = timeit('fib(23)', 'from __main__ import fib', number=1)
	t9 = timeit('fib(24)', 'from __main__ import fib', number=1)
	t10 = timeit('fib(27)', 'from __main__ import fib', number=1)
	t11 = timeit('fib(30)', 'from __main__ import fib', number=1)
	t12 = timeit('fib(33)', 'from __main__ import fib', number=1)
	t13 = timeit('fib(36)', 'from __main__ import fib', number=1)
	t14 = timeit('fib(39)', 'from __main__ import fib', number=1)
	t15 = timeit('fib(42)', 'from __main__ import fib', number=1)

	data = {
		'x':[1,3,6,9,12,15,18,21,23,24,27,30,33,36,39,42],
		'y':[1,2,8,34,144,610,2584,10946,28657,46368,196418,832040,3524578,14930352,63245986,267914296],
		'time':[t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15]
	}

	df = pd.DataFrame(data, columns=['x','y','time'])

	print(df)

	y = np.array([t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15])
	x = np.array([1,3,6,9,12,15,18,21,23,24,27,30,33,36,39,42])

	yp = None

	xi = np.linspace(x[0], x[-1],100)
	yi = np.interp(xi, x, y, yp)

	fig, ax = plt.subplots()
	ax.plot(x, y, 'o', xi, yi,)

	plt.grid()
	plt.title('Growth Rate Fibonacci')
	plt.xlabel('Fibonacci(x)')
	plt.ylabel('Time(seconds)')
	plt.savefig('crescimento_fibonacci.png')

	df.plot()
	plt.grid()
	plt.title('Growth Rate Fibonacci using Pandas')
	plt.xlabel('Time(seconds) and x value')
	plt.ylabel('y or Fibonacci(x)')
	plt.savefig('crescimento_fibonacci_pandas.png')
	
	plt.show()

	asdasd;
	


