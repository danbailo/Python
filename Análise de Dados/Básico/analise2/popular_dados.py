from random import uniform, randint

texto = []

def obterTexto():
    for _ in range(0,140):
        texto.append(
            str(uniform(1.50, 2.20)) + ';' +
            str(uniform(50, 120)) + ';' +
            str(randint(0,10)) + '\n'
        )

def gerarArquivo():
    with open('./peso.csv', 'w+', encoding='UTF-8') as entrada:
        obterTexto()
        entrada.writelines(texto)

if __name__ == "__main__":
    gerarArquivo()
    # print(texto)