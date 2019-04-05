# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:20:53 2019

@author: ecorrea
"""

#P077: Estatísticas sobre matrizes + Axis
import numpy as np  

#carrega o arquivo "NOTAS.csv" para uma matriz
notas = np.loadtxt('C:/CursoPython/NOTAS.csv', 
                    dtype=float,
                    skiprows=1,
                    delimiter=',') 

#imprime a matriz e gera as estatísticas
print('notas: ', notas) 

print('média geral: ', notas.mean()) 
print('média de cada prova: ', notas.mean(axis=0)) 
print('média de cada aluno: ', notas.mean(axis=1)) 

print('maior nota geral: ', notas.max()) 
print('maior nota de cada prova: ', notas.max(axis=0))
print('maior nota de cada aluno: ', notas.max(axis=1))