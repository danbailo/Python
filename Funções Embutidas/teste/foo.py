#problema 1
# Use o map para criar uma função que encontre o tamanho de cada palavra na frase (quebrado por espaços) e retornar os valores em uma lista.
# A função terá uma entrada de uma string e exibirá uma lista de números inteiros.

#problema 1 usando compreensao em listas
string = 'How long are the words in this phrase'
s = [len(i) for i in string.split(' ')]
print(s)

#problema 1 usando a resposta original
def word_lenghts(string):
    return list(map(len,string.split()))

print(word_lenghts(string))

#problema 1 usando lambda

print(list(map(len,string.split())))

#problema 2
# Use reduce para pegar uma lista de dígitos e retornar o número que eles correspondem a.

# Não converta os números inteiros em strings! *
from functools import reduce

lst = [3,4,3,2,1]
# 3*10 = 30 + 4 = 34
# 34*10 = 340 + 3 = 343
# 343*10 = 3430 + 2 = 3432
# 3432*10 = 34320 + 1 = 34321 
print(reduce(lambda x,y:x*10+y,lst))

#Problema 3
#Use o filter para retornar as palavras de uma lista de palavras que começam com uma letra especificada.

l = ['hello','are','cat','dog','ham','hi','go','to','heart']

# for i in l:
#     if i[0] == 'h':
#         print(i)

print(list(filter(lambda string:string[0]=='h',l)))

#Problema 4
#Use zip e list comprehension para retornar uma lista do mesmo comprimento onde cada valor é as duas cadeias de caracteres de L1 e L2 concatenados juntos com o conector entre eles. Veja o exemplo abaixo:

a = ['A','B']
b = ['a','b']

print(list(zip(a,b)))

        #desmebramento da tupla
four = [word1+'-'+word2 for (word1,word2) in zip(a,b)]

print(four)

#Problema 5
#Use enumerate e outras habilidades para retornar um dicionário que tenha os valores da lista como chaves e o índice como o valor. Você pode assumir que um valor só aparecerá uma vez na lista fornecida.

d_list = ['a','b','c']

# d = {'key1':'ponei'}

# print(d[0])

# print(list(enumerate(d_list)))

#pegando a tupla e mudando o valor do retorno para retornar um dict
d = {b:a for (a,b) in enumerate(d_list)}

print(d)

#Problema 6
#Use enumerar e outras habilidades de cima para retornar a contagem do número de itens na lista cujo valor é igual ao seu índice.

lst = [0,2,2,1,5,5,6,10]
i = 0
for (a,b) in enumerate(lst): 
    if a == b:
        i += 1
print(i)

x = len([a for (a,b) in enumerate(lst) if a == b])
print(x)