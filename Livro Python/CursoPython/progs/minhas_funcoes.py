# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:43:37 2019

@author: notebook
"""

#módulo "minhas_funcoes"
def faixa_etaria(idade):
    if (idade < 18) :
        return '<18'
    elif (idade >= 18 and idade < 30) :
        return '18-29'
    elif (idade >= 30 and idade < 40) :
        return '30-39'
    else :
        return '>=40'
