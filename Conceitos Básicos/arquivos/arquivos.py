#Abrindo um arquivo com Python

#Podemos abrir um arquivo com a função open(). 
#A função open também possui argumentos (também chamados de parâmetros). 

# Abre um arquivo txt já existente
my_file = open('test.txt')

print(my_file)
print(type(my_file))

# Agora podemos ler o arquivo
print(my_file.read())

#se tentar ler novamente
print(my_file.read())

#Isso acontece porque você pode imaginar que o "cursor" de leitura esteja no final do arquivo 
#depois de ter lido. Portanto, não há nada a ler. Podemos redefinir o "cursor" assim:

# Procure o início do arquivo (índice 0)
print(my_file.seek(0))

#se tentar ler novamente
print(my_file.read())

#Para não ter que reiniciar todas as vezes, também podemos usar o método readlines. 
# Tenha cuidado com arquivos grandes, já que tudo será mantido na memória. 
# Nós aprenderemos como iterar sobre arquivos grandes mais tarde no curso.

my_file.seek(0)

# Readlines retorna uma lista das linhas no arquivo.
print(my_file.readlines())

#Por padrão, usando a função open() só nos permitirá ler o arquivo, 
#precisamos passar o argumento 'w' para escrever sobre o arquivo

# Adiciona um segundo argumento à função, 'w', que significa escrita
other = open('new.txt','+w')

# Escreve no arquivo
other.write('This is a new line')

# Lê o arquivo
other.seek(0)
print(other.readlines())

iterate = open('iterate.txt')

for line in iterate:
    print(line)