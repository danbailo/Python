# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:40:34 2019

@author: notebook
"""

#P012: criando e utilizando uma funcao
def faixa_etaria(idade):
    if (idade < 18) :
        return '<18'
    elif (idade >= 18 and idade < 30) :
        return '18-29'
    elif (idade >= 30 and idade < 40) :
        return '30-39'
    else :
        return '>=40'

#chamando a função com diferentes valores para o parâmetro "idade"
a = faixa_etaria(15)
b = faixa_etaria(50)
c = faixa_etaria(35)

print(a); print(b); print(c)	
