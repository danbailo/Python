# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:54:07 2019

@author: notebook
"""

#P010: while com break + while com continue

print('-------------------------------------')
print('1-Exemplo de while com break:\n')
n=-1;
while (n < 21):
    n=n+1;
    if n%2 != 0: break #quebra o laço se n for ímpar... 
    print(n)

print('fim do while com break...\n')

print('-------------------------------------')
print('2-Exemplo de while com continue:\n')
n=-1;
while (n < 21):
    n=n+1;
    if n%2 != 0: continue #quebra a iteração se n for ímpar... 
    print(n)

print('fim do while com continue...\n')


