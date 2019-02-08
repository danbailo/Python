print('hello guys!')

a = len(('hello guys!'))

print(a)

s = 'Hello World'
print(s)

print(s[0])
print(s[1])
print(s[2])

# Retorna todos elementos a partir do elemento de indice 1
print(s[1:])

# Retorna tudo até o elemento de índice 3
print(s[:3])

# Tudo
print(s[:])

# Última letra (um índice antes do 0, então ele começa da parte de trás)
print(s[-1])

# Pega tudo, menos a última letra
print(s[:-1])

print('\n')

d = 'danielbailo'
# Pega tudo, de 1 em 1
print(d[::1])

# Pega tudo, mas os espaçamentos são de 2 em 2, basicamente, pula o elemento da frente
print(d[::2])

# Pega tudo, mas com passos negativos, de trás para frente.
print(d[::-1])
print('\n')


# strings em python são imutaveis
#s[0] = 'x' (dá erro!!!)

# concatenar strings

s = s + ' concatenate me!'

print(s)

#Podemos usar o símbolo de multiplicação para criar repetições!

letter = 'z'

print(letter*10)

#Métodos embutidos em strings

#coloca toda string em caixa alta
print(s.upper())


#coloca toda string em caixa baixa
print(s.lower())

# Divide uma string nos espaços em branco (este é o padrão)
print(s.split())

# Divide em um elemento específico (não inclui o elemento que foi dividido)
print(s.split('W'))

#Podemos usar o método .format() para adicionar objetos formatados a instruções de impressões.
print('Insert another string with curly brackets: {}'.format('The inserted string'))
print('\n')

#Strings avançados
print('Strings avançados')
s = 'hello world'
print(s)
print(s.capitalize())

#Localização e contagem
print(s.count('o')) #conta a quantidades de o
print(s.find('d')) #conta ate chegar no d

print('\n')
#Formatação
#
#O método center() permite que você coloque sua string 
#'centrada' entre uma string fornecida com um certo comprimento.
print(s.center(10,'z'))

#expandtabs() will expand tab notations \t into spaces:
print('hello\thi'.expandtabs(15))


print('\n')
#Métodos de verificação
s = 'hello'

#isalnum() retornará True se todos os caracteres em S forem alfanuméricos
print(s.isalnum())

#isalpha() retornará True se todos os caracteres em S forem alfabéticos
print(s.isalpha())

#islower() retornará True se todos os caracteres cased em S forem minúsculos, Falso caso contrário.
print(s.islower())

#isspace() retornará True se todos os caracteres em S forem espaços em branco.
print(s.isspace())

#isupper() retornará True se todos os caracteres encapsulados em S forem maiúsculos, Falso caso contrário.
print(s.isupper())

#Outro método é endswith() que é essencialmente o mesmo que uma verificação booleana em s[-1]
print(s.endswith('o')) #retorna true se a string termina com o

#Podemos usar split() para dividir a string em um determinado elemento e retornar uma lista do resultado.
print(s.split('e'))

#Podemos usar a partition() para retornar uma tupla que inclui o separador (a primeira ocorrência) e a primeira metade e a metade final.
print(s.partition('l'))