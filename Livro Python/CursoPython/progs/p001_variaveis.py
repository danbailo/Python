# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:04:33 2018

@author: notebook
"""

#P001: variáveis e tipos; funçoes type() e print()

#PARTE 1: declaração de variáveis
nome = 'Jane'
sobrenome = "Austen"
idade = 41
nota = 9.9
aprovado = True

#PARTE 2: imprimindo o conteúdo das variáveis e os tipos das mesmas
print(nome, sobrenome, idade, nota, aprovado)
print(type(nome)) 
print(type(sobrenome)) 
print(type(idade)) 
print(type(nota))
print(type(aprovado))

#PARTE 3: mudando o valor e o tipo da variável “nota”
nota = 'A'
print('mudei o valor e o tipo de "nota" para: ', nota, ",", type(nota))
