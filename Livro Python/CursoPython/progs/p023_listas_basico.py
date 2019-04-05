# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:13:03 2019

@author: notebook
"""

#P023: processamento básico de listas 
lst_bichos = ['bem-te-vi', 'capivara', 'saracura', 'teiú']

tam_lista = len(lst_bichos)   #nossa conhecida função len() pode ser utilizada p/
                              #obtermos o tamanho (número de elementos) da lista

#(1)-indexando os elementos
primeiro = lst_bichos[0]                 #retorna 'bem-te-vi'
ultimo = lst_bichos[3]                   #retorna 'teiú'
ultimo_tambem = lst_bichos[-1]           #também retorna 'teiú'

print('lst_bichos: ', lst_bichos)
print('tipo de dado: ', type(lst_bichos))
print("total de elementos: ", tam_lista)
print("primeiro elemento: " + primeiro)
print("último elemento: " + ultimo)
print("último elemento de novo: " + ultimo_tambem)
print('---------------')

#(2)-iteração: percorrendo os elementos com um laço for-range() 
k=1;
for b in lst_bichos:
    print('elemento ', k, ' = ', b)
    k = k+1
print('---------------')

#(3)-fatiamento: obtendo sublistas (slices)
print(lst_bichos[0:2])          #['bem-te-vi','capivara']
print(lst_bichos[2:4])          #['saracura','teiú']
print(lst_bichos[:2])           #['bem-te-vi','capivara']
print(lst_bichos[2:])           #['saracura','teiú']
print('---------------')

#(4)-operador in (busca): elemento pertence à lista?
tem_capivara = 'capivara' in lst_bichos 
tem_piton = 'píton' in lst_bichos 

print("'capivara' está na lista? -> ", tem_capivara)
print("'píton' está na lista? -> ", tem_piton)

#(5)-modificando o conteúdo 
lst_bichos[2] = 'sabiá'             #altera o elemento de índice 2
print("nova lista -> ", lst_bichos)
lst_bichos[:2] = ['bicudo','preá']  #altera os elementos 0 e 1 
print("novíssima lista -> ", lst_bichos)
