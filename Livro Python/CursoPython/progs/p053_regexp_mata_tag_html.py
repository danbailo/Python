# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 15:17:22 2019

@author: ecorrea
"""
#P052 remove html
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

nomeArq = 'C:/CursoPython/filmes.html'
f = open(nomeArq)
conteudo = f.read()

sem_html = cleanhtml(conteudo)

print(conteudo)
print('----------------------------------')
print(sem_html)

