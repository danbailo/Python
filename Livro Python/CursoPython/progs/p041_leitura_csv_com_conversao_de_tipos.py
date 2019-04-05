# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:51:19 2019

@author: notebook
"""

#P041: leitura de arquivo CSV + conversão de tipos
nomeArq = 'C:/CursoPython/FUNCIONARIOS.csv'
f = open(nomeArq)

for linha in f:
    linha = linha[:len(linha)-1] #remove o chato do "/n"
    lstAux = linha.split(";")
    nome = lstAux[0]
    idade = int(lstAux[1])
    salario = float(lstAux[2])
    if (idade > 49): 
       premio = salario * 0.15
       print(nome + " -> ganhou um premio de R$ " + str(premio))
