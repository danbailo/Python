# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:23:47 2019

@author: ecorrea
"""

#P078: operações de conjunto
import numpy as np  

v1 = np.array(["Fisher","Pearson","Turing", "Ada"])
v2 = np.array(["Fisher","Fisher","Ada","Ada"])

print(np.unique(v2))          #['Ada','Fisher']
print(np.in1d(v1,v2))         #[True, False, False, True]
print(np.intersect1d(v1,v2))  #['Ada','Fisher']
print(np.union1d(v1,v2))      #['Ada','Fisher','Pearson','Turing']
print(np.setxor1d(v1,v2))     #['Pearson','Turing']
