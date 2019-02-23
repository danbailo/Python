#Escreva uma função que calcula o volume de uma esfera dado seu raio.
def vol(rad):
    return (4*3.14*(rad**3))/3

print(vol(5))

#Escreva uma função que verifica se um número está em um determinado intervalo (inclusive o máximo e mínimo)
def ran_check(num,low,high):
    if num >= low and num <= high:
        print(num,'esta no intervalo entre {} e {}'.format(low,high))
    else:
        print(num,'NAO esta no intervalo entre {} e {}'.format(low,high))

ran_check(1,3,57)

#** Escreva uma função Python que aceita uma string e calcule o número de maiúsculas e minúsculas. **

def up_low(s):
    up = 0
    low = 0
    for char in s:
        if char.isupper():
            up += 1
        elif char.islower():
            low += 1      
        else:
            pass      
    print('caracteres maisculos',up)
    print('caracteres minusculos',low)

up_low('Olá Sr. Rogers, como você está bem, terça-feira?')

#** Escreva uma função Python que recebe uma lista e retorna uma nova lista com elementos exclusivos da primeira lista. **
def unique_list(l):
    return list(set(l))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

#** Escreva uma função Python para multiplicar todos os números em uma lista. **
def multiply(numbers):
    mult = 1
    for n in numbers:
        mult *= n
    return mult

print('a multiplicacao eh',multiply([1,2,3,-4]))

#** Escreva uma função Python que verifica se uma string passada é palindrome ou não. **
#Nota: Um palíndromo é palavra, frase ou seqüência que lê o mesmo para trás.
def palindrome(s):
    s = s.replace(' ','')
    return s == s[::-1]

print(palindrome('aaa'))

#Escreva uma função Python para verificar se uma string é um pangrama ou não.
#Nota: Pangramas são palavras ou frases contendo cada letra do alfabeto pelo menos uma vez.

import string
print(string.ascii_lowercase)

def ispangram(str1, alphabet=string.ascii_lowercase):
    num = len(alphabet)
    cont = 0

    for i in alphabet:
        if i in str1:
            cont += 1
    return cont == num

print(ispangram('h quicfox jumps over the lazy dog'))