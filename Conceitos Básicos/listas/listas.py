# Atribui uma lista a uma variável chamada my_list
my_list = [1,2,3]

print(my_list)
print(len(my_list))

my_list.pop()
print(my_list)

my_list = ['A string',23,100.232,'o']

print(my_list)

print(len(my_list))

#Indexação e corte
my_list = ['one', 'two', 'three', 4, 5]

# Pega o elemento de indice 0
print(my_list[0])

print('Indexação')
# Pegue o índice 1 e tudo depois
print(my_list[1:]) #intervalo fechado

print(my_list[:2]) #intervalo aberto -> so printa até o indice x<2

print(my_list[::-1]) #reverso

#Nós também podemos usar + para concatenar listas, assim como fizemos por strings.
print(my_list + ['new item'])
print(my_list)

print('\n')
# Reassign
my_list = my_list + ['add new item permanently']
print(my_list)

print(my_list * 2)


print('\n')

print('metodos basicos')
#métodos básicos
#
# Cria a lista
l = [1, 2, 3]
print(l)

# append -> adiciona item permanente a no final da lista
l.append('append me!')
print(l)

# pop -> por padrao tira um item no final da lista
l.pop()
print(l)

l.pop(0)
print(l)

# Atribui o elemento retirado, lembre-se de que o índice padrão é -1
popped_item = l.pop()

print(l)
print(popped_item)

lista = [1, 2, 3, 4, 4, 1, 1]
print(lista)

#count () retorna o número de vezes que um elemento ocorre na sua lista
print(lista.count(1))

x = [1, 2, 3]
x.extend([4,2]) #append adicionaria mais uma lista dentro da lista
print(x)

#Index retornará o índice de qualquer elemento que seja colocado como um argumento.
#Nota: Se o elemento não estiver na lista, um erro será retornado.
print('indice:',x.index(2))

#insert pega dois argumentos: 
# insert(índice, objeto) Este método coloca o objeto no índice fornecido.
print(x)
x.insert(1,150)
print(x)

#O método remove() remove a primeira ocorrência de um valor.
x.remove(2)
print(x)

print('\n')
#Podemos usar o método sort e os métodos ** reverse ** para alterar suas listas:
new_list = ['a', 'e', 'x', 'b', 'c']
print(new_list)

# Use o reverso para reverter a ordem (isto é permanente!)
new_list.reverse()
print(new_list)

# Use ordenar para classificar a lista (neste caso, ordem alfabética)
new_list.sort()
print(new_list)

print('\n')
print('Listas aninhadas')
#Uma ótima característica das estruturas de dados do Python é que eles suportam * aninhamento *.
#Isso significa que podemos ter estruturas de dados dentro das estruturas de dados. 
#Por exemplo: uma lista dentro de uma lista.

# Começamos com 3 listas
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

print('lista 1 ->',lst_1)
print('lista 2 ->',lst_2)
print('lista 3 ->',lst_3)
# Faça uma lista de listas para formar uma matriz
matrix = [lst_1,lst_2,lst_3]

print(matrix)
print(matrix[0]) # lista 1 no indice 0

# Pegue o segundo item do primeiro item no objeto da matriz
print(matrix[0][1]) # elemento 1 na lista 1 que esta no indice 0

print('\n')
#Compreensão de listas

# Crie uma lista de compreensão desconstruindo um loop for dentro de um []
first_col = [row[0] for row in matrix] # o resultado e uma lista apenas com os elementos [0]
									###de cada lista
print(first_col)

lista = [1, 1, [1, 2]]
print(lista[2][1])



