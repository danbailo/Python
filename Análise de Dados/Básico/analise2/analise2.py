import numpy as np
import matplotlib.pyplot as plt

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
print()
print('Mín:', tabelaIMC(np.amin(imc))) #min retorna o msm
print('Máx:', tabelaIMC(np.amax(imc))) #max retorna o msm
print('Máx - Mín:', tabelaIMC(np.ptp(imc)))
print()
#media tradicional, termo medio ao longo do vetor
print('Média:', tabelaIMC(np.median(imc)))
print('Média por Força:', tabelaIMC(np.average(imc)))
print('Média Aritmética:', tabelaIMC(np.mean(imc)))
print()
print('Desvio Padrão:', np.std(imc))
print('Variância:', np.var(imc))
print()

print('='*50)
print(' '*22+'Percentil')
print('='*50)
print('IMC Médio do 1º Percentil:',tabelaIMC(np.median(np.percentile(imc, q=range(0,25)))))
print('IMC Médio do 2º Percentil:',tabelaIMC(np.median(np.percentile(imc, q=range(25,50)))))
print('IMC Médio do 3º Percentil:',tabelaIMC(np.median(np.percentile(imc, q=range(50,75)))))
print('IMC Médio do 4º Percentil:',tabelaIMC(np.median(np.percentile(imc, q=range(75,100)))))

y = [
    np.median(np.percentile(imc, q=range(0,25))),
    np.median(np.percentile(imc, q=range(25,50))),
    np.median(np.percentile(imc, q=range(50,75))),
    np.median(np.percentile(imc, q=range(75,100)))
]
x = [1, 2, 3, 4]

plt.plot(x,y)
plt.title("Percentil dos IMC da População")
plt.ylabel("Valor")
plt.xlabel("Percentil")
plt.grid()
plt.savefig('percentil.png')
plt.show()