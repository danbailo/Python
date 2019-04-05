# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:52:04 2019

@author: notebook
"""

#P025: métodos disponíveis para listas
numeros = [0, 10, 15, 10, 20]
print("lista original: ", numeros)

quantos_10 = numeros.count(10) #retorna 2
print("num. de ocorrências do valor 10: ", quantos_10)

i_10 = numeros.index(10) #retorna 1
print("índice da primeira ocorrência de 10: ", i_10)

numeros.append(5)    #adiciona o valor 5 no final da lista
print("lista modificada1: ", numeros)

numeros.insert(1,1000) #insere 1000 como segundo elemento
print("lista modificada4: ", numeros)

numeros.remove(10) #remove o primeiro elemento 10
print("lista modificada3: ", numeros)

numeros.extend([50, 60]) #adiciona a lista [50, 60] no final
print("lista modificada5: ", numeros)

numeros.sort() #ordena
print("lista ordenada: ", numeros)

numeros.reverse() #inverte
print("lista reversa: ", numeros)

numeros.clear() #esvazia a lista
print("lista vazia: ", numeros)
