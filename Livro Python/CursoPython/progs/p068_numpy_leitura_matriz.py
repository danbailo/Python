# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:33:02 2019

@author: ecorrea
"""

#P068 Populando uma matriz a partir de um arquivo texto 
import numpy as np

#carrega o arquivo para uma matriz
m_dist = np.genfromtxt('C:/CursoPython/DISTANCIAS.csv', 
                    skip_header=1, 
                    dtype=np.float16,
                    delimiter=',') 

#imprime a matriz
print('m_dist: ', m_dist) 