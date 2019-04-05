# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 13:27:19 2019

@author: notebook
"""

#P018: funções pré-definidas

#funções numéricas
n1=100
n2=3.141592653
n3=9.99

print(abs(1000), abs(-500), abs(2 * -2.5), abs(0)) #1000  500  5.0  0
print(pow(n1,2))                                   #10000
print(round(n2,2))                                 #3.14
print(round(n2), round(n3))                        #3  10

#funções de conversão
s1='5'
s2='9.99'

print(int(s1))   #converteu '5' -> 5
print(float(s2)) #converteu '9.99' -> 9.99
print('O valor de PI com 10 digitos é: ' + str(n2))  
print('O valor de PI com 2 digitos é: ' + str(round(n2,2)))

#funções de string
s1='python'
s2='inconstitucional'

print(len(s1))   #6
print(len(s2))   #16
print(max(s1))   #'y'
print(min(s1))   #'h'

