from random import uniform, randint

texto = []

def obterTexto():
    for _ in range(0,100):
        texto.append(
            str(uniform(1.50, 2.20)) + ';' +
            str(uniform(50, 120)) + ';' +
            str(randint(0,10)) + '\n'
        )

def gerarArquivo():
    arq = './peso.csv'
    entrada = open(arq, 'w+', encoding='UTF-8')
    obterTexto()
    entrada.writelines(texto)
    entrada.close()

if __name__ == "__main__":
    gerarArquivo()
    # print(texto)