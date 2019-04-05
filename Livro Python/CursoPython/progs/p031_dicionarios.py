# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 18:56:33 2019

@author: notebook
"""

#P031: Dicionário: criação e manipulação básica
dic_alunos = {'M01':'Hane','M13':'George','M15':'Thomas'}
print('dic_alunos (original): ', dic_alunos) 


#insere novo aluno (novo par chave:valor)
dic_alunos['M04'] = 'Aldous' 

#altera o valor associado à chave 'M01' para Jane
dic_alunos['M01'] = 'Jane' 

#remove o elemento de chave 'M15'
del dic_alunos['M15'] 

#checando se uma chave existe 
tem_M13 = 'M13' in dic_alunos         #retorna True
tem_M99 = 'M99' in dic_alunos         #retorna False
print('dic_alunos (após alterações): ', dic_alunos) 
print('tipo de dado: ', type(dic_alunos)) 
print('existe a mat. M13?: ', tem_M13)
print('existe a mat. M99?: ', tem_M99)
