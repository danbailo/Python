# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 16:08:05 2019

@author: notebook
"""

#P094: Criando e Removendo Colunas em um DataFrame
#     (usando o Python padrão)
import pandas as pd  

#(1)-Importa CSV para o DataFrame
pessoas = pd.read_csv('C:/CursoPython/pessoas.csv')
print('* * DataFrame original:')           
print(pessoas)           
print('---------------------------------------')

#(2)-Remove linhas em função de um teste lógico
pessoas = pessoas.drop(pessoas[pessoas.idade>40].index)
print('* * DataFrame sem as pessoas que têm mais de 40 anos:')           
print(pessoas)           
print('---------------------------------------')

