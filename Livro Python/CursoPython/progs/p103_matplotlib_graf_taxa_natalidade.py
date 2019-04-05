# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 22:31:39 2019

@author: notebook
"""

#P103: Taxa Bruta de Natalidade
import matplotlib.pyplot as plt
import numpy as np  

#carrega o arquivo para uma matriz
m = np.loadtxt('C:/CursoPython/TX_NATALIDADE.csv', 
                    skiprows=1, dtype=float, delimiter=',')

#cria um vetor c/ dados da 1a coluna (Ano) e um outro com os da 2a (Taxa)
x = np.array(m[:,0],dtype=np.int32) 
y = m[:,1] 

#plota a linha na cor vermelha
plt.plot(x, y, color='red')

#plota os pontos como círculos (parâmetro 'ro'... existem outros) marrons
plt.plot(x, y, 'ro', color='brown')

#define a escala dos eixos X e Y
plt.ylim(min(y)*0.9, max(y)*1.05)
plt.xlim(2000,2015)

#define os "xticks" do eixo X
#(se não colocar fica bem feio, pois ele exibe 2000.5, 2001.5, ...)
plt.xticks(np.arange(2000, 2015, 2))

#define o título do gráfico
plt.title('Taxa Bruta de Natalidade por mil habitantes – Brasil – 2000 a 2015')   

#define os rótulos
plt.xlabel('Ano')                       #rótulo do eixo X
plt.ylabel('Taxa por mil habitantes')   #rótulo do eixo Y

#finalmente, mostra o gráfico
plt.show()