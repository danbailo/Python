# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:39:47 2019

@author: ecorrea
"""

 #P070: percorrendo as células de uma matriz 
import numpy as np

#(1)-carrega o arquivo para uma matriz
m_dist = np.genfromtxt('C:/CursoPython/DISTANCIAS.csv', 
                    skip_header=1, 
                    dtype=np.float16,
                    delimiter=',') 

#(2)-imprime as distâncias entre cada cidade
for i in range(0, m_dist.shape[0]):     #percorre as linhas
    for j in range(0, m_dist.shape[1]): #percorre as colunas
        if (i < j):
            msg = 'Dist. de C' + str(i+1) + ' para C' + str(j+1)
            print(msg + " = " + str(m_dist[i,j]))