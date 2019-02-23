#Vamos ver como construir a sintaxe de uma função em Python. Ela tem a seguinte forma:
def name_of_function(arg1,arg2):
    '''
    A documentação da função ficará aqui
    '''
    # Faça coisas aqui
    return # retorne o resultado desejado aqui

def say_hello():
    print('hello world!')

say_hello()

def greeting(name):
    print('Hello, %s' %name)

greeting('Daniel')

#usando return

def soma(a,b):
    return a+b

print(soma('a','1'))

def is_prime(num):
    '''
    Método para checar se é primo
    '''
    for n in range(2,num):
        if num % n == 0:
            print('Não primo')
            break
    else: # Se o módulo nunca for zero, é primo
        print('Primo')
    
is_prime(17)

import math

def is_prime2(num):
    '''
    Melhor método para checar primos
    '''
    if num % 2 == 0 and num > 2: 
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

print(is_prime2(17))