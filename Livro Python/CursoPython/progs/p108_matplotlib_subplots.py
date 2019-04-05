# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 23:26:09 2019

@author: notebook
"""

#P108: Subplots 
import matplotlib.pyplot as plt
import numpy as np  

x = np.arange(1,101)
y1 = np.sqrt(x)
y2 = np.log2(x)

#configura o tamanho da figura
#o primeiro parâmetro é a largura e o segundo a altura
fig = plt.figure(figsize=(10,5))

#configura um subplot com 1 linha e 2 colunas
#seta a primeira coluna como ativa para receber o gráfico y1 = raiz(x)
plt.subplot(1,2,1)
plt.plot(x, y1, 'b^') #'b^' = triângulos azuis
plt.title("y = raiz(x)")

#adiciona o segundo subplot, ativando a coluna 2
plt.subplot(1,2,2)
plt.plot(x, y2, '--g') #'g--' = linha verde pontilhada
plt.title("y = log2(x)")
