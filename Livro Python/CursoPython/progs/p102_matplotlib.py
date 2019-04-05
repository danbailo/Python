# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 22:06:55 2019

@author: notebook
"""

#P102: Olá Matplotlib! 

#importa o submódulo "pyplot" do pacote "matplotlib", 
#renomeando-o para "plt" 
import matplotlib.pyplot as plt
import numpy as np  

x = np.arange(1,11)
y = 2 * x  + 5
  
plt.title('y = 2x + 5')            #título do gráfico
plt.xlabel('meu querido eixo X')   #rótulo do eixo X
plt.ylabel('meu querido eixo Y')   #rótulo do eixo Y

plt.plot(x,y)                    #plota os dados
plt.show()                       #mostra o gráfico
