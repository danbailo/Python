import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 20)
print(x)
y = np.sin(x)
print(y)
yp = None
xi = np.linspace(x[0], x[-1])
print(xi)
yi = np.interp(xi, x, y, yp)
print(yi)

fig, ax = plt.subplots()
ax.grid()
ax.plot(x, y, 'o', xi, yi,)
plt.show()