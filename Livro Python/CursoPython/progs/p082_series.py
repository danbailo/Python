# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 11:24:36 2019

@author: notebook
"""

 #P082: Olá Series! 
import pandas as pd  

#(1)-criação de Series especificando os dados (em uma lista), 
#    mas sem especificar o vetor índices.
#    nesse caso os índices serão inteiros de 0 a n-1 
#    (onde n é o número de elementos da lista)
s1 = pd.Series([70, 30, -1, 50, 0])

#ao imprimir, os índices são mostrados à esquerda e os valores à direita
print('s1:') 
print(s1)             #[0:70, 1:30, 2:-1, 3:50, 4:0]

#(2)-indexação, fatiamento  e aritmética funcionam como na ‘NumPy’
#    o detalhe IMPORTANTE é que o mapeamento índice-valor é preservado
print('-------------------------------------------')
print(s1[s1 > 0])     #[0:70, 1:30, 3:50]
print('\n') 
print(s1[2:4]);       #[2:-1, 3:50]
print('\n') 
print(s1*2);          #[0:140, 1:60, 2:-2, 3:100, 4:0]

#(3)-criação da Series onde índices=siglas de países e valores=nome da moeda
siglas = ['BR','FR','UK','IT','US']
moedas = ['Real','Euro','Libra','Euro','Dólar']
s2 = pd.Series(moedas,index=siglas)

print('-------------------------------------------')
print('s2:') 
print(s2) 

#(4)-podemos utilizar os rótulos para indexar 
print('-------------------------------------------')
print(s2['UK'])           #'Libra'
print('\n') 
print(s2[['BR','IT']])    #['BR':'Real', 'IT':'Euro']
print('\n') 
print(s2[1:3])            #['FR':'Euro', 'UK':'Libra']
print('\n') 
print('BR' in s2)         #True
print('AR' in s2)         #False

 #P082: Olá Series! 
import pandas as pd  

#(1)-criação de Series especificando os dados (em uma lista), 
#    mas sem especificar o vetor índices.
#    nesse caso os índices serão inteiros de 0 a n-1 
#    (onde n é o número de elementos da lista)
s1 = pd.Series([70, 30, -1, 50, 0])

#ao imprimir, os índices são mostrados à esquerda e os valores à direita
print('s1:') 
print(s1)             #[0:70, 1:30, 2:-1, 3:50, 4:0]

#(2)-indexação, fatiamento  e aritmética funcionam como na ‘NumPy’
#    o detalhe IMPORTANTE é que o mapeamento índice-valor é preservado
print('-------------------------------------------')
print(s1[s1 > 0])     #[0:70, 1:30, 3:50]
print('\n') 
print(s1[2:4]);       #[2:-1, 3:50]
print('\n') 
print(s1*2);          #[0:140, 1:60, 2:-2, 3:100, 4:0]

#(3)-criação da Series onde índices=siglas de países e valores=nome da moeda
siglas = ['BR','FR','UK','IT','US']
moedas = ['Real','Euro','Libra','Euro','Dólar']
s2 = pd.Series(moedas,index=siglas)

print('-------------------------------------------')
print('s2:') 
print(s2) 

#(4)-podemos utilizar os rótulos para indexar 
print('-------------------------------------------')
print(s2['UK'])           #'Libra'
print('\n') 
print(s2[['BR','IT']])    #['BR':'Real', 'IT':'Euro']
print('\n') 
print(s2[1:3])            #['FR':'Euro', 'UK':'Libra']
print('\n') 
print('BR' in s2)         #True
print('AR' in s2)         #False

#(5)-Insere Portugal e Japão e Remove os Estados Unidos e França
print('-------------------------------------------')
s2['PT'] = 'Euro'
s2['JP'] = 'Iene'
s2 = s2.drop(labels=['US','FR'])
print(s2)

#(6)-Os métodos values e index retornam, respectivamente, os valores 
#    e índices da Series, respectivamente
print('-------------------------------------------')
print(s2.values)          #['Real' 'Libra' 'Euro' 'Euro' 'Iene']
print(s2.index)           #Index(['BR', 'UK', 'IT', 'PT', 'JP'], dtype='object')
