# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 23:16:50 2019

@author: notebook
"""

#P106: Histograma
from matplotlib import pyplot as plt  
import pandas as pd

#(1)-carrega o arquivo CSV para um DataFrame
d = pd.read_csv('C:/CursoPython/GRANJAS.csv', delimiter=';') 

#(2)-carrega o arquivo CSV para um DataFrame
t = d.iloc[:,1].values

#(3)-plota o histograma com 8 bins
num_bins = 8
plt.hist(t, num_bins)
plt.title('Histograma')
plt.show()

