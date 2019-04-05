# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 11:31:52 2019

@author: notebook
"""

#P083: Series - alinhamento automático + alteração de índices por atribuição
import pandas as pd  

#(1)-Alinhamento automático
s1 = pd.Series([10,20,30],index=['A','B','C'])
s2 = pd.Series([1,2,3,4],index=['A','B','C','D'])
s3 = s1+s2
print(s3)       

#(2)-Alteração de índices
print('-------------------------------------------')
s3.index = ['i','j','k','l'] #muda os índices de ['A','B','C','D']
                             #para ['i','j','k','l']

print(s3)       
