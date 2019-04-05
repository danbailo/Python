# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 17:19:02 2019

@author: notebook
"""

#P096: Fatiamento de DataFrames
import numpy as np  
import pandas as pd  

#(1)-Cria um DataFrame com 4 linhas e 5 colunas
d = pd.DataFrame(np.arange(20).reshape(4,5), 
                 index=['L1','L2','L3','L4'], columns=['A','B','C','D','E']) 
print('* * DataFrame "d":')           
print(d)           

#(2)-Atribuição por rótulos
print('---------------------------------------')
print('* * Fatiamento por rótulos com "loc":')           
print(d.loc['L2',['B','C']])   #pega a linha 'L2', colunas 'B' e 'C'
print('---------------------------------------')
print(d.loc[:,['A','D','E']])  #pega todas as linhas, colunas 'A', 'D' e 'E'
print('---------------------------------------')
print(d.loc[['L1','L4'],:])    #pega todas as colunas das linhas 'L1' e 'L4'

#(3)-Atribuição por índices
print('---------------------------------------')
print('* * Fatiamento por índices com "iloc":')           
print(d.iloc[0:3,3:5])   #pega as linhas 0 a 2 (L1, L2, L3), colunas 3 e 4 (D, E)
print('---------------------------------------')
print(d.iloc[:,3:5])     #pega todas as linhas, colunas 3 e 4
print('---------------------------------------')
print(d.iloc[0:3,:])     #pega todas as colunas, linhas 0 a 2

#(4)-Atribuição normal
d.iloc[1,2] = 700    #muda o valor da linha L2, coluna C para 700

#(5)-Atribuição com fatiamento
#substitui os valores das linhas 0 a 2 (L1, L2, L3), colunas 3 e 4 (D, E)
#pelos valores contidos em uma matriz 3x2
d.iloc[0:3,3:5]=np.arange(1000,1006).reshape(3,2)
print('---------------------------------------')
print(d)