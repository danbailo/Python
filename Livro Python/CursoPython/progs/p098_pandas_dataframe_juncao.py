# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 21:00:50 2019

@author: notebook
"""

#P098: junção de DataFrames
import pandas as pd    

#(1)-importa os CSVs
emp = pd.read_csv('C:/CursoPython/EMPRESAS.csv', encoding='ansi')
ul = pd.read_csv('C:/CursoPython/ULS.csv', encoding='ansi')

print('EMP: '); print(emp)
print('------------------------------------------------')
print('UL: '); print(ul)
print('------------------------------------------------')

#(2)-Combina os Arquivos

#2.1 INNER JOIN
c1 = pd.merge(emp, ul, how='inner', on='raiz')
print('resultado do INNER JOIN: ')
print(c1)
print('------------------------------------------------')

#2.2 LEFT JOIN
c2 = pd.merge(emp, ul, how='left', on='raiz')
print('resultado do LEFT JOIN: ')
print(c2)
print('------------------------------------------------')

#2.3 FULL OUTER JOIN
c3 = pd.merge(emp, ul, how='outer', on='raiz')
print('resultado do FULL OUTER JOIN: ')
print(c3)
print('------------------------------------------------')
