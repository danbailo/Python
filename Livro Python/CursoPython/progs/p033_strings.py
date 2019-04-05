# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 12:17:49 2019

@author: notebook
"""

#P033: processamento básico de strings
palavra = 'Tiê Sangue'

#(1) indexando caracteres
prim_letra = palavra[0]                  #retorna 'T'
ult_letra = palavra[len(palavra)-1]      #retorna 'e'
tot_letras = len(palavra)                #retorna 10 
print(prim_letra,ult_letra,tot_letras)
print('----------------------------------------')

#(2) obtendo segmentos ou fatias (slices)
print(palavra[0:3])                      #'Tiê'
print(palavra[4:11])                     #'Sangue'
print(palavra[:3])                       #'Tiê'
print(palavra[4:])                       #'Sangue'
print(palavra[-1])                       #'e' (última letra)
print(palavra[-2])                       #'u' (penúltima letra)
print('----------------------------------------')

#(3) percorrendo a string letra por letra, através de um laço
tot_esp = 0
for letra in palavra:
	print(letra)
	if letra == ' ':
		tot_esp = tot_esp + 1
print('"' + palavra + '" possui ' + str(tot_esp) + ' espaço(s)')
print('----------------------------------------')
    	
#(4) operador "in"
tem_a = 'a' in palavra      #'Tiê Sangue' possui a letra 'a'?
tem_b = 'b' in palavra      #'Tiê Sangue' possui a letra 'b'?
print(tem_a, tem_b);
