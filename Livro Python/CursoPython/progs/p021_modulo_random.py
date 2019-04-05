# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 14:15:05 2019

@author: notebook
"""

 #P021: módulo ‘random’ 
import random

#(1)-função randint()
for i in range(6):
    n = random.randint(1,61) #próximos números da mega-sena???
    print(n)

#(2)-função choice()
k = random.choice([1,2,3,4,5])
print(k)

#(3)-trabalhando com sementes
#quando a semente não é especificada, o Python usa o timestamp do sistema
#e os valores de n1 e n2 mudarão sempre que o programa for executado
n1=random.random()
n2=random.random()
print(n1, n2)

#Mas se você especifica a semente, a série de números será sempre a mesma:
estado = random.getstate()
random.seed(2019)

x1=random.random()   #0.8323...
x2=random.random()   #0.7889...
print(x1, x2)

random.setstate(estado)

#IMPORTANTE: para poder "desabilitar" a semente (voltar ao valor default, ou seja
#o timestamp do sistema), é preciso utilizar a receita mostrada acima:
# 
# 1 -> capturar o estado defaut do gerador (que é o timestamp do sistema), 
#      usando getstate()
# 2 -> mudar a semente com seed()
# 3 -> retornar ao estado default do gerador usando setstate
