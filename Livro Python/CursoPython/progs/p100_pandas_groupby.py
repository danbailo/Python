# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 22:25:42 2019

@author: notebook
"""

#P100: groupby()
import pandas as pd  

#(1)-Cria do DataFrame "projetos"
dados = {'codigo': ['P1','P2','P3','P4','P5','P6'],
         'tipo': ['A','A','B','A','B','A'],
         'local': ['RJ','DF','RJ','DF','RJ','SP'],
         'custo': [500000,900000,150000,1000000,None,850000]}

projetos = pd.DataFrame(dados)
print(projetos)
print('-----------------------------------')

#(2)-Gera uma variável "grouped" onde a chave é "tipo" e a medida "custo"
grupo_custo_tipo = projetos['custo'].groupby(projetos['tipo'])

#(3)-Computa agregados a partir da variável gerada
print('- média de custo, por tipo de projeto: ',grupo_custo_tipo.mean())
print('-----------------------------------')
print('- tot. de proj c/ custo definido, por tipo:', grupo_custo_tipo.count())
