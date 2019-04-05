# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 20:03:24 2019

@author: notebook
"""

#P097: Funções estatísticas em DataFrames
import pandas as pd  

#(1)-Importa CSV para o DataFrame
palestras = pd.read_csv('C:/CursoPython/palestras.csv', index_col="dia")
print('* * DataFrame original:')           
print(palestras)           
print('---------------------------------------')

#(2)-Computa as estatísticas por coluna 
print('* * média de público por linguagem:\n ', palestras.mean(), '\n')   
print('* * soma  de público por linguagem:\n ', palestras.sum(), '\n')   

#(3)-Computa as estatísticas por linha
print('* * média de público por dia:\n ', palestras.mean(axis=1), '\n')   
print('* * soma  de público por dia:\n ', palestras.sum(axis=1), '\n')   
