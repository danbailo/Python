# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 17:07:27 2019

@author: notebook
"""

#P095: Ordenando um DataFrame por uma ou mais colunas
import pandas as pd  

#(1)-Importa CSV para o DataFrame
pessoas = pd.read_csv('C:/CursoPython/pessoas.csv')
print('* * DataFrame original:')           
print(pessoas)           
print('---------------------------------------')

#(2)-Ordena por salário e idade (ascendente)
pessoas = pessoas.sort_values(by=['salario','idade'], ascending=[True,False])
print('* * DataFrame ordenado por salário e idade:')           
print(pessoas)           
print('---------------------------------------')

