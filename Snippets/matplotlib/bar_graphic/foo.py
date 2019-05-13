import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 20] #onde esta as barras
y = [2, 3, 5, 3, 7, 9] #tamanho das barras, eixo y

plt.title("Gráfico de Barras")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.bar(x,y)
plt.show()
