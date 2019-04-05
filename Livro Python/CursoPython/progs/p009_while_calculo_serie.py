# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:51:32 2019

@author: notebook
"""

#P009: repetição com o comando while (segundo exemplo)
N = 5; H = 1
i = 1 #variável de controle

print('* * * cálculo de H = 1 + (1 / 2) + (1 / 3) + ... + (1 / N), dado N =',N)

while (i !=N):
    i = i + 1
    H = H + (1 / i)

print('* * * resposta: H = ', H)

