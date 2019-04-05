# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:51:32 2019

@author: notebook
"""

#P008: repetição com o comando while (primeiro exemplo)
c = -20
print('Tabela de conversão de graus Celsius para graus Fahrenheit')
while c <= 100:
    f=c*1.8 + 32
    print(c,'ºC ----> ',f,'ºF')
    c=c+10

print('\nFIM!!!')
