# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 23:10:58 2019

@author: notebook
"""

#P105: Gráfico de Dispersão 
import matplotlib.pyplot as plt
import numpy as np  

#carrega o arquivo para uma matriz
m = np.loadtxt('C:/CursoPython/TRIANGLE.csv', 
                    dtype=float, delimiter=',')

#cria um vetor para cada coluna
x = m[:,0]  #eixo x
y = m[:,1]  #eixo y

#a classe tem que ser "int", para que o uso do colormap seja possível
classe = np.array(m[:,2],dtype=np.int16) 

#configura e plota o gráfico
plt.figure(figsize=(10,10))
colormap = np.array(['red', 'lime', 'pink','blue'])
plt.scatter(x, y, c=colormap[classe], s=40)
plt.title('Grafico de Dispersão')
plt.show()
