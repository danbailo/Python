# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 18:43:03 2019

@author: notebook
"""

#P011: repetição com for-range()
print('\n* * imprimindo de 0 a 9')
for i in range(10):
   print(i) 

print('\n* * imprimindo de 100 a 105')
for i in range(100, 106):
   print(i)  
   
print('\n* * 0 a 15, usando 5 como incremento')
for i in range(0, 16, 5):
   print(i)  
   
print('\n* * ordem reversa: 5, 4, 3, 2, 1')
for i in range(5, 0, -1):
   print(i) 
