# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 14:47:14 2019

@author: notebook
"""

#P101: Carregando dados do Censo de Washington para DataFrame 
import pandas as pd    

#(1)-importa o DataFrame
nomeArq = 'C:/CursoPython/CENSUS.csv'
df = pd.read_csv(nomeArq)

#(2)-alguns métodos
#imprime as primeiras linhas
print('head():'); 
print(df.head()) 
print('-------------------')

#imprime as últimas linhas
print('tail():'); 
print(df.tail()) 
print('-------------------')

#checando os rótulos das colunas e dos índices
print('index:'); 
print(df.index)        #inteiro, 0 a 50 com passo 1

print('columns:'); 
print(df.columns)      #object: ['age', 'education', ..., 'class']
print('-------------------')

#checando os tipos das colunas
print('dtypes:'); 
print(df.dtypes) 
print('-------------------')

#checando os dados na "camada NumPy" (camada "por trás" do DataFrame)
print('values')
print(df.values)
print('-------------------')

#(3)-método describe()
print('describe')
print(df.describe())