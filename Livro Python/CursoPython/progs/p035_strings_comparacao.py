# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 12:45:13 2019

@author: notebook
"""

#P035: comparação de strings
p1 = 'pássaro'
p2 = 'PÁSSARO'
p3 = '123'
print(p1=='pássaro')          #True
print(p1=='PáSSaRo')          #False
print(p1==p2)                 #False
print(p1.lower()==p2.lower()) #True
print(p3 < p1)                #True 

p1 = 'áaa'
p2 = 'aaa'
p3 = 'AAA'
print(p1==p2)                 #False
print(p2 < p1)                #True
print(p2 < p3)                #False
