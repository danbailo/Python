#O módulo de coleções é um módulo interno que implementa tipos de dados de contêiner 
# especializados que fornecem alternativas aos contêineres incorporados de uso geral da Python. 
# Nós já abordamos os conceitos básicos: dict, list, set e tuple.

#Counter
#Counter * é uma subclasse * dict * que ajuda a contar objetos hash-able. Dentro disso, os 
# elementos são armazenados como chaves de dicionário e as contagens dos objetos são armazenadas
#  como o valor.

from collections import Counter

l = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
print(Counter(l))

s = 'aabsbsbsbhshhbbsbs'
print(Counter(s))

s = 'How many times does each word show up in this sentence word times each each word'
words = s.split()
print(Counter(words))

# Métodos com Counter()
c = Counter(words)

print(c.most_common(2)) #retorna a qtd em ordem decrescente os mais incidentes

list_of_pairs = []

n = 1

sum(c.values())                 # total de todas as contagens
c.clear()                       # redefinir todas as contagens
list(c)                         # elementos exclusivos da lista
set(c)                          # converter para um conjunto
dict(c)                         # converter para um dicionário regular
c.items()                       # converter para uma lista de pares (elem, cnt)
Counter(dict(list_of_pairs))    # converter de uma lista de pares (elem, cnt)
c.most_common()[:-n-1:-1]       # n elementos menos comuns
c += Counter()                  # remove zero e contagens negativas

from collections import defaultdict
#defaultdict é um dicionário como objeto que fornece todos os métodos fornecidos pelo dicionário,
#  mas leva o primeiro argumento (default_factory) como tipo de dados padrão para o dicionário.
#  Usar defaultdict é mais rápido do que fazer o mesmo usando o método dict.set_default.

#** Um defaultdict nunca gerará um KeyError. Qualquer chave que não existe obtém o valor 
# retornado pela fábrica padrão. **

# d = {}

# d['one'] #keyerror

d  = defaultdict(object)
print(d['one'])

for item in d:
    print(item)

#Também pode inicializar com valores padrão:
d = defaultdict(lambda: 0)
print(d['one'])

#OrderedDict
#Um OrderedDict é uma subclasse de dicionário que lembra a ordem em que seu conteúdo é 
# adicionado.

print('Normal dictionary:')

d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)

from collections import OrderedDict


print('OrderedDict:')

d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print (k, v)

# Igualdade com um Dicionário Ordenado
# Um dicionario normal olha para seu próprio conteúdo quando testa por igualdade. 
# Um OrderedDict também considera a ordem em que os itens foram adicionados.

print('Dictionaries are equal?')

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

print (d1 == d2)

print('Dictionaries are equal? ')

d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'


d2 = OrderedDict()

d2['b'] = 'B'
d2['a'] = 'A'

print( d1 == d2)

# namedtuple
# A tupla padrão usa índices numéricos para acessar seus membros, por exemplo:
t = (12,13,14)
print(t[0])

#Para casos de uso simples, isso geralmente é suficiente. Por outro lado, lembrar qual índice 
# deve ser usado para cada valor pode levar a erros, especialmente se a tupla tiver muitos 
# campos e for construída longe de onde ela é usada. Um namedtuple atribui nomes, bem como o 
# índice numérico, a cada membro.
#Cada tipo de namedtuple é representado por sua própria classe, criado usando a função de 
# fábrica namedtuple(). Os argumentos são o nome da nova classe e uma string contendo os 
# nomes dos elementos.
#Você basicamente deve pensar o namedtuple como uma maneira muito rápida de criar um novo 
# tipo de objeto / classe com alguns campos de atributos. Por exemplo:

from collections import namedtuple

Dog = namedtuple('Dog','age breed name')

sam = Dog(age=2,breed='Lab',name='Sammy')

frank = Dog(age=2,breed='Shepard',name="Frankie")

#Construímos o namedtuple primeiro passando o nome do tipo de objeto (Dog) e depois passando 
# uma string com a variedade de campos como uma string com espaços entre os nomes dos campos. 
# Podemos chamar os vários atributos:

print(Dog)
print(sam)
print(sam[0])
print(sam.age)

#Conclusão
#Esperemos que você veja agora quão incrivelmente útil o módulo de coleções está em Python
#  e deve ser o seu módulo de acesso para uma variedade de tarefas comuns!