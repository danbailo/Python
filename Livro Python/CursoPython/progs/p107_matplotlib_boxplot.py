# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 16:32:35 2019

@author: notebook
"""

#P107: Boxplot
import matplotlib.pyplot as plt
import numpy as np

dados = np.array([3, 7, 2, 1, 4, 3, 8, 3, 5, 7, 4, 5, 6, 7, 6, 5, 4, 3, 9, 5])

plt.boxplot(dados)
plt.title('Boxplot muito básico')
plt.show()