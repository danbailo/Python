# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# Make a fake dataset
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))

plt.bar(y_pos, height, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
plt.xticks(y_pos, bars, rotation=90)

#adiciona margem
#plt.subplots_adjust(bottom=0.4, top=0.99)

plt.show()
