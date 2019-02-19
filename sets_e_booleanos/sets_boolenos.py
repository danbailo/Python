#sets(conjuntos)
#Os conjuntos são uma coleção não ordenada de elementos únicos. Podemos construí-los usando a função set(). 
#Avançemos e façamos um conjunto para ver como funciona

x = set()

print(type(x))

print(x)
# Adicionamos elementos com o método add().
x.add(1)

print(x)

#Observe os colchetes. Isso não indica um dicionário! Embora você possa montar analogias como um
#set sendo um dicionário com apenas chaves. Sabemos que um conjunto tem apenas entradas únicas. 

# Adiciona um elemento novo
x.add(2)
print(x)

#Remove todos os elementos do conjunto
x.clear()
print(x)

x = {1,2,3}
#Retorna uma cópia do set. Observe que é uma cópia, então as mudanças no original não afetam a cópia.
s = x.copy()
print('este é o x', x)
print('este é o s', s)

#Retorna a diferença de dois ou mais sets. A sintaxe é:
#set1.difference(set2)

x.add(4)

print('diferença de x e s',x.difference(s))

#Sintaxe difference_update() é:
#
# set1.difference_update (set2)
#o método retorna set1 depois de remover elementos encontrados no set2

s1 = {1,2,3}
s2 = {1,4,5}

print(s1.difference_update(s2))

print(s1)

#discard()
#Remove um elemento de um conjunto se for um membro. Se o elemento não for um membro, não faça nada.
x = {1,2,3,4,5}
print(x)
x.discard(3)
print(x)

#Retorna a interseção de dois ou mais sets como um novo sets. (Isto é, elementos comuns a todos os sets).
s1 = {1,2,3}
s2 = {1,2,4}
s3 = s1.intersection(s2)
print(s3)

print(s1)
s1.intersection_update(s2)
print(s1)
print(s2)

#Esse método retornará True se dois conjuntos tiverem uma interseção nula.
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}

print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

#Este método informa se outro conjunto contém este conjunto.
print(s1.issubset(s2))

#Este método informará se este set contém outro set.
print(s2.issuperset(s1))

#Retorna a diferença simétrica de dois sets como um novo set. (Isto é, todos os elementos que estão exatamente em um dos sets)
s3 = s1.symmetric_difference(s2)

print(s3)

#Retorna a união de dois sets (ou seja, todos os elementos que estão no set).
print('uniao',s1.union(s2))

#Atualize um set com a união de si e outros.
print('antes do update',s1)
s1.update(s2)
print('dps do update',s1)





x.add(1)
x.add(2)
x.add(3)
x.add(1)
x.add(1)
print(x)

#Observe como ele não colocará mais 1 lá. Isso porque um conjunto apenas se ocupa de elementos 
#exclusivos! Podemos transformar uma lista com múltiplos elementos 
#repetidos para um conjunto para obter os elementos exclusivos

# Cria uma lista com elementos repetidos
l = [1,1,2,2,3,4,5,6,1,1]

print(set([1,1,2,2,3,4,5,6,1,1]))

#booleanos

# Define um objeto como True
a = True

print(a)

print(1>2)

b = None

print(b)