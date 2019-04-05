# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 14:08:57 2019

@author: notebook
"""

#P091: importa XLS para DataFrame
import pandas as pd    

#importa o data frame
nomeArq = 'C:/CursoPython/WEATHER.xls'
df = pd.read_excel(nomeArq)

#checando a importação
print('index:'); print(df.index); print('--------------')
print('columns:'); print(df.columns); print('--------------')
print('dtypes:'); print(df.dtypes); print('--------------')
print(df)
