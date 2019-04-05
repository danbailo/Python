# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 16:45:54 2019

@author: notebook
"""

#P109: salvando uma figura

#este exemplo está em https://matplotlib.org/users/pyplot_tutorial.html
# desenha três gráficos na mesma figura
import matplotlib.pyplot as plt
import numpy as np  

x = np.arange(0., 5., 0.2)
plt.plot(x, x, 'r--', x, x**2, 'bs', x, x**3, 'g^')

#salva em um arquivo "png" com o método savefig()
plt.savefig("C:/CursoPython/figura1.png")
