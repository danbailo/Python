import numpy as np

def tabelaIMC(imc):
    if imc < 16:
        return str(imc) + ': Magreza grave'
    elif imc < 17:
        return str(imc) + ': Magreza moderada'
    elif imc < 18.5:
        return str(imc) + ': Magreza leve'
    elif imc < 25:
        return str(imc) + ': Saudável'
    elif imc < 30:
        return str(imc) + ': Sobrepeso'
    elif imc < 35:
        return str(imc) + ': Obesidade Grau I'     
    elif imc < 40:
        return str(imc) + ': Obesidade Grau II(severa)'
    else:
        return str(imc) + ': Obesidade Grau III(mórbida)'
                  
#desempacota os dados num np.array, no caso, tres np.array
altura, peso, forca = np.loadtxt('./peso.csv',
                                delimiter=';',
                                unpack=True,
                                dtype='float')

imc = peso / altura**2

print('Mín: '+tabelaIMC(np.amin(imc))) #min retorna o msm
print('Máx: '+tabelaIMC(np.amax(imc))) #max retorna o msm
print('Máx - Mín: '+tabelaIMC(np.ptp(imc)))