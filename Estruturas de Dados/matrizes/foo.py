#uma matriz bidimensional, nada mais é do que uma lista de lista
matriz = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
]
#matriz[linha][coluna]
# print(matriz[0][-1])

def print_matriz(matriz):
    for i in matriz:
        for j in i:
            print(str(j) + '\t', end = '')
        print('')   

print_matriz(matriz)