# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 12:37:12 2019

@author: notebook
"""

#P034: métodos de strings
p1 = 'Lagarto Teiú'

p1_maiusc = p1.upper()       
p1_minusc = p1.lower()       

num_letras_p1 = len(p1)    
num_letras_a = p1.count('a')    
testa_endswith = p1.endswith('rto',4,7)    
testa_find = p1.find('a')    
testa_rfind = p1.rfind('a')    

p1_troca = p1.replace('a','o')
p1_split = p1.split()

p2 = '  Capivara ';
teste_strip = p2.strip();

p3 = 'ei, olha isso... uma capivara!'
sem_pontuacao = p3.translate(p3.maketrans('','',",.!")) #remove: , . !

print("p1.upper()= " + p1_maiusc)
print("p1.lower()= " + p1_minusc)
print("len(p1)= " + str(num_letras_p1))
print("p1.count('a')= " + str(num_letras_a))
print("p1.endswith('rto',4,7)= ",testa_endswith)
print("p1.find('a')= ",testa_find)
print("p1.rfind('a')= ",testa_rfind)
print("p1.replace('a','o')= " + p1_troca)
print("p1.split()= ", p1_split)
print("p2.strip()= *" + teste_strip + "*")
print("frase com pontuacao= " + p3)
print("frase sem pontuacao= " + sem_pontuacao)
