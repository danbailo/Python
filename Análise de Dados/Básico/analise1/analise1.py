import numpy as np

altura = [1.72, 1.56, 1.45, 1.56, 1.65, 1.70]
peso = [86.5, 48.0, 56.0, 70.5, 80.2, 65.7]

# imc = peso/altura**2 #causa um erro, pois e necessario um iteravel para realizar essa operacao

npAltura = np.array(altura)
npPeso = np.array(peso)

imc = npPeso/npAltura**2

print(imc)