# As expressões lambda nos permitem criar funções "anônimas". Isso basicamente significa que 
#podemos criar funções ad hoc sem necessidade de definir corretamente uma função usando def.

#Os objetos de função retornados executando expressões lambda funcionam exatamente como os 
# criados e atribuídos por defs. Há diferença fundamental que torna a lambda útil em 
# papéis especializados: O corpo de lambda é uma expressão única, não um bloco de declarações.

#O corpo da lambda é semelhante ao que colocamos na declaração de retorno do corpo def. 
# Simplesmente escrevemos o resultado como uma expressão em vez de devolvê-lo explicitamente. 
# Como é limitado a uma expressão, um lambda é menos geral que uma def. 
# Só podemos espremer o design, para limitar o aninhamento do programa. 
# O lambda foi projetado para codificar funções simples e def manipula as tarefas maiores.

#Vamos montar lentamente uma expressão lambda, desconstruindo uma função:

#exemplo de func q calculca o quadrado do n
def square(num):
    result = num**2
    return result

print(square(2))

#quebrando mais
def square2(num):
    return num**2

print(square2(3))

#Nós podemos realmente escrever isso em uma linha (embora seja uma forma ruim para fazê-lo)
def square3(num): return num**2

print(square3(4))

#Essa é a forma de uma função que uma expressão lambda pretende replicar. Uma expressão lambda 
#pode então ser escrita como:

square4 = lambda num: num**2

print(square4(5),'\n')
####################

par = lambda num: num%2==0

print(par(2))
print(par(3))

soma = lambda num1,num2: num1+num2

print(soma(3,7))

char = lambda a:a[0]

print(char('Daniel'))
print(char([1,2,3]))


rev = lambda s: s[::-1]
print(rev('daniel'))
print('\n')