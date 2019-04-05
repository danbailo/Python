# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:44:17 2019

@author: ecorrea
"""

#P071: operações aritméticas com vetores matrizes 
import numpy as np  

#operações entre vetor e escalares
v1 = np.array([0,5,10]) 
print('v1*2 = ', v1 * 2)           #[0, 10, 20]
print('v1-1 = ', v1 - 1)           #[-1, 4, 9]
print('v1**3 = ', v1 ** 3)         #[0, 125, 1000]

#soma dois vetores com 3 elementos
print('-------------------------------------------')
x = np.array([0,5,10]) 
y = np.array([1,2,3]) 
z = x + y
print('z = ', z)                 #[1, 7, 13]

#soma duas matrizes 2x4
m1 = np.ones((2,4),dtype=np.int16)
m2 = np.array([[1,2,3,4],[5,6,7,8]]) 
print('-------------------------------------------')
print('m1 = ', m1)
print('m2 = ', m2)
print('m1 + m2 = ', m1 + m2)   

#subtração um vetor de 4 posições de uma matriz 3 x 4
m3 = np.ones((3,4),dtype=np.int16)
v2 = np.arange(4) 
print('-------------------------------------------')
print('m3 = ', m3)
print('v2 = ', v2)
print('m3 - v2 = ', m3 - v2)   

#multiplicação de duas matrizes “a” e “b” com shape 4 x 2
#IMPORTANTE: não se trata da multiplicação matricial!!!!!
#Na verdade, c[0,0] receberá a[0,0] * b[0,0]; c[0,1] receberá a[0,1] * b[0,1] 
#e assim sucessivamente.
a=np.array([[1,2,3,4], [5,6,7,8]])
b=np.array([0,2,4,6,8,10,12,14])
b=b.reshape(2,4)
c=a*b

print('-------------------------------------------')
print('a = ', a)
print('b = ', b)
print('c = a*b =', c)