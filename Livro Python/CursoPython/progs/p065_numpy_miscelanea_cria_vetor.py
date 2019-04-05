# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:19:55 2019

@author: ecorrea
"""

 #P065: Miscelânea de métodos para criar vetores NumPy
import numpy as np  

n1 = np.array([1,2,3]); n2 = np.array([4,5])

#com o método append() podemos combinar vetores
n3 = np.append(n1, n2) 
print(n3)              #[1 2 3 4 5]

#arange(): versão NumPy da função range do Python
a1 = np.arange(11)       #seq. de 0 a 10
a2 = np.arange(0, 16, 5) #seq. de 0 a 15, com 5 como incremento
a3 = np.arange(5, 0, -1) #seq. de 5 a 1

print('-------------------------------------------')
print('a1 = ', a1)       #[0,1,2,3,4,5,6,7,8,9,10]
print('a2 = ', a2)       #[0, 5, 10, 15]
print('a3 = ', a3)       #[5, 4, 3, 2, 1]

#repeat(): gera sequência de valores repetidos
#ones(): gera sequencia de valores 1
#zeros(): gera sequencia de valores 0
rep1 = np.repeat(100,5)
o1 = np.ones(5)
z1 = np.zeros(5)

print('-------------------------------------------')
print('rep1 = ', rep1)   #[100 100 100 100 100] 
print('o1 = ', o1)       #[1. 1. 1. 1. 1.] 
print('z1 = ', z1)       #[0. 0. 0. 0. 0.] 

#linspace(): gera elementos "uniformemente espaçados" entre o
#            início e o fim da sequência (neste caso, o valor final é incluído)
ls1 = np.linspace(1,3,9)       #seq. de 1 a 3, com 9 elementos
ls2 = np.linspace(0,2.0/3,4)   #seq. de 0 a 2/3, com 4 elementos

print('-------------------------------------------')
print("ls1 = ", ls1) #[1.  1.25  1.5  1.75  2.  2.25  2.5  2.75  3.]
print("ls2 = ", ls2) #[0., 0.22222222, 0.44444444, 0.66666667]
