import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(0,10,10)
y = np.random.randint(0,10,10)

plt.title('Scatterplot ou Gŕafico de pontos/disperssão')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.scatter(x,y, label='Pontos', color='orange')
plt.plot(x,y)

plt.grid()
plt.legend()
plt.show()
