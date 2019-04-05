# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 13:53:29 2019

@author: notebook
"""

#P089: Utilizando expressão regular para definir um delimitador
import pandas as pd  

log = pd.read_csv('C:/CursoPython/log.txt', 
              sep='\s+', 
              names = ["dia","hora", "login", "status"])

print(log) 
