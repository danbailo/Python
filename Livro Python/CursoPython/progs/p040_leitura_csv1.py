# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:43:40 2019

@author: notebook
"""

#P040: leitura de arquivo separado por delimitador
nomeArq = 'C:/CursoPython/CEPS.csv'
f = open(nomeArq)

aux=0  #auxiliar para permitir que cabeçalho seja ignorado
for linha in f:
    if (aux > 0): #ignora a linha de cabeçalho
        linha = linha[:len(linha)-1] #remove o tremendamente chato do "/n"
        lstPalavras = linha.split(",")
        cep_ini = lstPalavras[0]
        cep_fim = lstPalavras[1]
        uf = lstPalavras[2]
        print(uf + " -> CEPS de " + cep_ini + " a " + cep_fim)
    aux=aux+1
