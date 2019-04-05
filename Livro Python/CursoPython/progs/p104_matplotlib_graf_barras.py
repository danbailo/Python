# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 22:50:06 2019

@author: notebook
"""

#P104: Gráfico de Barras
import matplotlib.pyplot as plt
import pandas as pd  

#carrega o arquivo para uma matriz
d = pd.read_csv('C:/CursoPython/cinto.csv')

#aumenta o tamanho do gráfico (nomes das categorias são longos)
plt.figure(figsize=(10,5))

#plota com as categorias no eixo X e a porcentagem no eixo Y
plt.bar(d['usa_cinto'], d['porcentagem'])

#associa um label para o Eixo Y e coloca o título no gráfico
plt.ylabel('porcentagem')
plt.title('Uso do cinto de segurança pelos homens')

#mostra o gráfico
plt.show()
