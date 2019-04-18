import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from timeit import timeit

# (Public) Returns F(n).
def fibonacci(n):
	if n < 0:
		raise ValueError("Negative arguments not implemented")
	return _fib(n)[0]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = _fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)

if __name__ == "__main__":
	t0 = timeit('fibonacci(10)', 'from __main__ import fibonacci', number=1)
	t1 = timeit('fibonacci(100)', 'from __main__ import fibonacci', number=1)
	t2 = timeit('fibonacci(200)', 'from __main__ import fibonacci', number=1)
	t3 = timeit('fibonacci(300)', 'from __main__ import fibonacci', number=1)
	t4 = timeit('fibonacci(400)', 'from __main__ import fibonacci', number=1)
	t5 = timeit('fibonacci(500)', 'from __main__ import fibonacci', number=1)
	t6 = timeit('fibonacci(600)', 'from __main__ import fibonacci', number=1)
	t7 = timeit('fibonacci(650)', 'from __main__ import fibonacci', number=1)
	t8 = timeit('fibonacci(750)', 'from __main__ import fibonacci', number=1)
	t9 = timeit('fibonacci(850)', 'from __main__ import fibonacci', number=1)
	t10 = timeit('fibonacci(905)', 'from __main__ import fibonacci', number=1)
	t11 = timeit('fibonacci(1050)', 'from __main__ import fibonacci', number=1)
	t12 = timeit('fibonacci(1200)', 'from __main__ import fibonacci', number=1)
	t13 = timeit('fibonacci(1300)', 'from __main__ import fibonacci', number=1)
	t14 = timeit('fibonacci(1400)', 'from __main__ import fibonacci', number=1)
	t15 = timeit('fibonacci(1500)', 'from __main__ import fibonacci', number=1)

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