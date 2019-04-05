import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*3, 10)
print(x)
y = np.sin(x)
print(y)
xvals = np.linspace(0, 2*3, 10)
print(xvals)
yinterp = np.interp(xvals, x, y)
print(yinterp)
plt.plot(x, y, 'o')
plt.plot(xvals, yinterp, '-x')
plt.show()