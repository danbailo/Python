# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:33:25 2019

@author: ecorrea
"""

#P080: Álgebra Linear
import numpy as np  

#(1)-Obtendo a Matriz Transposta
print('-------------------------------------------')
m = np.array([0,6,-1,2,5,0])
m = m.reshape((3,2));

print('matriz original 2x3:\n',m);
print('matriz transposta 3x2:\n',m.T);

#(2)-Multiplicação de Matrizes
print('-------------------------------------------')
a = np.array([2,3,1,0,4,5]); a = a.reshape(3,2)
b = np.array([1,2,3,4]); b = b.reshape(2,2)
c = np.dot(a,b)
print('a =\n',a); print('b =\n',b); print('c =\n',c);