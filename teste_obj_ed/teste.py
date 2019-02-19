#Escreva uma breve descrição de todos os seguintes tipos de objetos e estruturas de dados sobre os quais aprendemos:

#Números: 

#Strings:

#Listas: 

#Tuplas:

#Dicionários:   

#Números
#Escreva uma equação que use multiplicação, divisão, expoente, adição e subtração igual a 100.25;
print('Multiplicação -', 10025*0.01)
print('Divisão -', 10025/100)
print('Expoente -', 100.25**1)
print('Adição -', 100+0.25)
print('Subtração -', 100.50-0.25)

print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 * 5)

print(type(3 + 1.5 + 4))

print('Quadrado de um número, elevar por 0.5\n')

#Strings
#Dada a string 'hello', dê um comando de índice que retorna 'e'. Use o código abaixo:
s = 'hello'
print(s[1])

#Inverta a string 'hello' usando indexação:
print(s[::-1])

#Dado o exemplo de linha, dê dois métodos para produzir a letra 'o' usando a indexação.
print(s[4])
print(s[-1],'\n')

#Listas
#Crie esta lista [0,0,0] duas formas diferentes.
l = [0,0,0]
lista = [0]*3

print(l)
print(lista)

#Altere o 'hello' da lista para 'goodbye'
l = [1,2,[3,4,'hello']]

l[2][2] = 'goodbye'

print(l)

#Ordene a lista:
l = [5,3,4,6,1]

l.sort() #ou sorted(l) - o sort altera permanentemente, o sorted nao

print(l,'\n')

#Dicionários
#Usando chaves e indexação, pegue o 'hello' dos seguintes dicionários:
d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d4 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d1['simple_key'])

print(d2['k1']['k2'])

print(d3['k1'][0]['nest_key'][1][0])

print(d4.keys())
print(d4['k1'][2]['k2'][1]['tough'][2][0])

#Você pode classificar um dicionário? Por que ou por que não?
#R: Não! Dicionários normais são mapeamentos não uma sequência.
#mapeamentos sempre vai ter uma associação entre chaves e valores e sequencia 
#sempre a posicao e o valor
print('\n')

#Tuplas
#Qual é a principal diferença entre as tuplas e as listas?
#R: Lista é mutavel e tupla é imutavel

#Como você cria uma tupla?
#R: t = (0,0,0)

#Conjuntos(set)
#O que é único em um conjunto?
#R: os elementos

#Use um conjunto para encontrar os valores exclusivos da lista abaixo:
l = [1,2,2,33,4,4,11,22,3,3,2]
print(set(l),'\n')

#Booleans
# Responda antes de executar a célula
print(2 > 3)
# Responda antes de executar a célula
print(3 <= 2)
# Responda antes de executar a célula
print(3 == 2.0)
# Responda antes de executar a célula
print(3.0 == 3)
# Responda antes de executar a célula
print(4**0.5 != 2)

#Pergunta final: qual é a saída booleana do bloco de código abaixo?
# Duas listas aninhadas
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# Verdadeiro ou falso?
print(l_one[2][0] >= l_two[2]['k1'])