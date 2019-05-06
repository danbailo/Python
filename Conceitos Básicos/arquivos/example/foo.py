with open('somefile.txt', 'w') as f:
    for i in range(10):
        f.write(str(i)+'\n')

#um arquivo é um objeto iteravel

with open('somefile.txt', 'r') as f:
    print(f.readline()) #a somente a primeira linha do arquivo
    f.seek(0) #reseta pra posicao inicial do arquivo, no caso o 0, antes dele ser fechado precisa fazer isso
    print(f.read()) #le todo o arquivo
    f.seek(0)
    print(f.readlines()) #le o arquivo de forma original