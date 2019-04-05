# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 20:13:40 2019

@author: notebook
"""

#P006: if, elif, else
idade = 25

if (idade < 18):  
    faixa_etaria = '<18'
elif (idade >= 18 and idade < 30):  
    faixa_etaria = '18-29'
elif (idade >= 30 and idade < 40):  
    faixa_etaria = '30-39'
else:  
    faixa_etaria = '>=40'

print('Se a idade é', idade, 'então a faixa etária é :', faixa_etaria)


