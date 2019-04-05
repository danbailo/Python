# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:08:29 2018

@author: notebook
"""

#P002: matemática básica

#Adição, subtração, multiplicação e divisão
x=5; y=2
print(x+y, x-y, x*y, x/y)
print(y**x)

#quociente e resto (ou módulo)
quociente = x // y
modulo = x % y
print("O quociente da divisão de", x, "por", y, "é: ", quociente)
print("O módulo da divisão de", x, "por", y, "é: ", modulo)

#expressão com parênteses
e1 = (1 + 2) * 5**2 / ((5-3) + 1)
print("O valor da expressão e1 é: ", e1)

#a divisão de dois inteiros sempre gera um float 
#(mesmo que a divisão seja exata)
a=10; b=5; c=a/b
print(a, b, c)
print(type(a), type(b), type(c)) 
