# Problema 1
#Crie um gerador que gere os quadrados de números até um número N.

def sqrt(number):
    for n in range(0,number):
        yield n**2

for x in sqrt(10):
    print(x)
print(list(sqrt(10)))

#Problema 2
#Crie um gerador que produza "n" números aleatórios entre um número baixo e alto (que são entradas). Nota: use a biblioteca random.
print('\n')

import random

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)
print('\n')
#Problema 3
#Use a função iter() para converter a string abaixo

s = 'hello'

s = iter(s)

print(next(s))

#Problema 4
#Explique um caso de uso para um gerador usando uma declaração yield onde você não deseja usar uma função normal com uma declaração de retorno.

#R: Se a saída tiver o potencial de ocupar uma grande quantidade de memória e você deseja apenas iterar através dela, você gostaria de usar um gerador.

my_list = [1,2,3,4,5]

#se eu usasse [], seria uma lista, logo essa sintaxe e para geradores
gencomp = (item for item in my_list if item > 3)

# print(list(gencomp))

for item in gencomp:
    print(item)

print(type(gencomp))