#Em Python, as tuplas são muito semelhantes às listas, no entanto, ao contrário das listas, 
# elas são imutáveis, o que significa que elas não podem ser alteradas. 
# Você usaria tuplas para apresentar coisas que não deveriam ser alteradas,
# como dias da semana ou datas em um calendário.

#A construção de tuplas usa () com elementos separados por vírgulas.

t = (1,2,3)

print(t)

# O método len() funciona também para tuplas
print(len(t))

# Você também pode variar os tipos de dados
t = ('one',2)

# E a indexação funciona exatamente como nas listas
print(t[0])

# Corte de dados também...
print(t[-1])

#Métodos básicos da Tupla
#As tuplas têm métodos internos, mas não tantas quanto listas. Vamos ver dois deles:

# Use .index com o valor de parâmetro para retornar o índice do mesmo
print(t.index('one'))

# Use .count() para saber quantas vezes determinado elemento apareceu na tupla
print(t.count('one'))

#Imutabilidade
#Como mencionado anteriormente, tuplas são imutáveis:

#t[0]= 'change' "error"

#Quando usar tuplas
#Você pode estar se perguntando: Por que se preocupar em usar tuplas quando eles têm 
# menos métodos disponíveis? Para ser honesto, as tuplas não são usadas tantas vezes como 
# listas na programação, mas são usadas quando a imutabilidade é necessária. 
# Se no seu programa você está passando por um objeto e precisa ter certeza de 
# que ele não seja alterado, então a tupla se tornará sua solução. 
# Ele fornece uma fonte conveniente de integridade de dados.
