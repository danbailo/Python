# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 21:24:24 2019

@author: notebook
"""

#P099: Concatenação de DataFrames
import pandas as pd  

#(1)-Cria dois DataFrames, "vendas1" e "vendas2"
vendas1 = pd.DataFrame({'produto':['café','suco','chá'],
                       'mes':['jan','jan','jan'],
                       'quant':[1200,350,245]}) 

vendas2 = pd.DataFrame({'produto':['café','suco','chá','guaraná'],
                       'mes':['fev','fev','fev','fev'],
                       'quant':[1512,487,300,408]}) 

vendas = pd.concat([vendas1,vendas2], ignore_index=True)

print(vendas)
