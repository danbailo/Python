# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:07:08 2019

@author: ecorrea
"""

#P074: indexação booleana
import numpy as np  

vet_filmes = np.array(['Procura Insaciável (1971)', 
    'Um Estranho no Ninho (1975)', 
    'Hair (1979)', 
    'Na Época do Ragtime (1981)', 
    'Amadeus (1984)', 
    'Valmont - Uma História de Seduções (1989)',  
    'O Povo Contra Larry Flint (1996)', 
    'O Mundo de Andy (1999)', 
    'Sombras de Goya (2006)',
    'Dobre placená procházka (2009)'])

vet_notas = np.array([7.4, 8.7, 7.6, 7.3, 8.3, 7.0, 7.3, 7.4, 6.9, 6.7])

vet_selecionados = vet_filmes[vet_notas > 7.5]

print(vet_selecionados)