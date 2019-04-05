# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 14:22:02 2019

@author: notebook
"""

#P022: print() revisitado
a=1
b=2
c=3

#imprime os valores de "a", "b" e "c" separados por espaço
print(a,b,c)           #1 2 3

#parâmetro "sep": troca espaço pelo separador especificado 
print(a,b,c,sep=';')   #1;2;3

#o operador especial %s permite a criação de uma saída formatada
#ele possui dois operandos: a string formatada e um valor
v=3.14
print("PI=%s" % v)     #PI=3.14 

#o sinal de escape (%) também permite a impressão de aspas
print("Imprimindo aspas \"")     #imprimindo aspas "
print('Imprimindo aspas \'')     #imprimindo aspas '

#adicionando quebras de linha com \n
print("linha1\nlinha2\nlinha3")

#separando valores por tabulação
print("coluna1\tcoluna2\tcoluna3")
