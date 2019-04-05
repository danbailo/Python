# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 13:08:48 2019

@author: notebook
"""

#P084: Series - carregando a partir de CSV e 
#      computando estatísticas sobre valores
import pandas as pd  

#(1)-carrega o CSV para uma Series
temperaturas = pd.read_csv('C:/CursoPython/temperaturas.csv', 
              sep=';', 
              index_col = 0,
              squeeze = True)

#(2)-imprime os dados
print(temperaturas)       
print(type(temperaturas))

#(3)-computa estatísticas do mesmo jeito que faríamos com um ndarray
print('valor máximo=',temperaturas.max())       
print('valor mínimo=',temperaturas.min())       
print('valor médio=',temperaturas.mean())       
