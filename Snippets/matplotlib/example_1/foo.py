import numpy as np
import matplotlib.pyplot as plt

# Create random data (x,y)
x = np.random.rand(200)
y = np.random.rand(200)
x2 = np.random.rand(150)
y2 = np.random.rand(150)

#a list of 200 values from 0 until 1
#print(x)

plt.scatter(x, y)
plt.scatter(x2, y2)

plt.show()


