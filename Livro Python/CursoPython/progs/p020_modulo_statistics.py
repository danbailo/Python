# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 13:57:40 2019

@author: notebook
"""

 #P020: módulo ‘statistics’ 
import statistics as s

nomes_filmes = ['Procura Insaciável (1971)', 
    'Um Estranho no Ninho (1975)', 
    'Hair (1979)', 
    'Na Época do Ragtime (1981)', 
    'Amadeus (1984)', 
    'Valmont - Uma História de Seduções (1989)',  
    'O Povo Contra Larry Flint (1996)', 
    'O Mundo de Andy (1999)', 
    'Sombras de Goya (2006)',
    'Dobre placená procházka (2009)']

avaliacao_filmes = [7.4, 8.7, 7.6, 7.3, 8.3, 7.0, 7.3, 7.4, 6.9, 6.7]

        
print('média = ',s.mean(avaliacao_filmes))        
print('mediana = ',s.median(avaliacao_filmes))        
print('variância = ',s.variance(avaliacao_filmes))        
print('desvio padrão = ',s.stdev(avaliacao_filmes)) 
