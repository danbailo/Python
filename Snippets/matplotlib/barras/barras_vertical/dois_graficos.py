import matplotlib.pyplot as plt

x1 = [0,2,4,6,9,10]
y1 = [1,3,5,7,10,2]

x2 = [1,3,5,7,8,12]
y2 = [4,5,2,3,6,11]

plt.title("Gráfico de Barras Duplo")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.bar(x1, y1, label="Gráfico 1")
plt.bar(x2, y2, label="Gráfico 2")
plt.legend()

plt.show()