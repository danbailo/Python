import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from timeit import timeit

def fib(n):
    a, b = 0, 1
    for _ in range(0, n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
	t0 = timeit('fib(10)', 'from __main__ import fib', number=1)
	t1 = timeit('fib(100)', 'from __main__ import fib', number=1)
	t2 = timeit('fib(200)', 'from __main__ import fib', number=1)
	t3 = timeit('fib(300)', 'from __main__ import fib', number=1)
	t4 = timeit('fib(400)', 'from __main__ import fib', number=1)
	t5 = timeit('fib(500)', 'from __main__ import fib', number=1)
	t6 = timeit('fib(600)', 'from __main__ import fib', number=1)
	t7 = timeit('fib(650)', 'from __main__ import fib', number=1)
	t8 = timeit('fib(750)', 'from __main__ import fib', number=1)
	t9 = timeit('fib(850)', 'from __main__ import fib', number=1)
	t10 = timeit('fib(905)', 'from __main__ import fib', number=1)
	t11 = timeit('fib(1050)', 'from __main__ import fib', number=1)
	t12 = timeit('fib(1200)', 'from __main__ import fib', number=1)
	t13 = timeit('fib(1300)', 'from __main__ import fib', number=1)
	t14 = timeit('fib(1400)', 'from __main__ import fib', number=1)
	t15 = timeit('fib(1500)', 'from __main__ import fib', number=1)

	data = {
		'x':[10,100,200,300,400,500,600,650,750,850,905,1050,1200,1300,1400,1500],
		'time':[t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15],
		# 'y':[1,2,8,34,144,610,2584,10946,28657,46368,196418,832040,3524578,14930352,63245986,267914296]
	}

	# df = pd.DataFrame(data, columns=['x','y','time'])
	df = pd.DataFrame(data, columns=['x','time'])

	print(df)

	y = np.array([t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15])
	x = np.array([10,100,200,300,400,500,600,650,750,850,905,1050,1200,1300,1400,1500])

	yp = None

	xi = np.linspace(x[0], x[-1],100)
	yi = np.interp(xi, x, y, yp)

	fig, ax = plt.subplots()
	ax.plot(x, y, 'o', xi, yi,)

	plt.grid()
	plt.title('Growth Rate Fibonacci Iterative')
	plt.xlabel('Fibonacci(x)')
	plt.ylabel('Time(seconds)')
	plt.savefig('crescimento_fibonacci_iterativo.png')

	df.plot()
	plt.grid()
	plt.title('Growth Rate Fibonacci Iterative using Pandas')
	plt.xlabel('Time(seconds) and x value')
	plt.ylabel('y or Fibonacci(x)')
	plt.savefig('crescimento_fibonacci_pandas_iterativo.png')
	
	plt.show()