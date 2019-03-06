#Os decoradores podem ser pensados como funções que modificam a * funcionalidade * de outra 
# função. Eles ajudam a tornar seu código mais curto e mais "Pythonico".

s = 'Global Variable'

def func():
    print(locals()) #nao tem nenhuma funcao ou variavel local
    return 1

print(func())

# print(globals())

print(globals().keys())

print(globals()['s'])

#vamos continuar construindo a lógica do que é um decorador. Lembre-se que em Python 
# ** tudo é um objeto **. Isso significa que as funções são objetos a qual podem ser 
# atribuídos etiquetas e passados para outras funções. Comece com alguns exemplos simples:
print('\n')
def hello1(name='Jose'):
    return 'Hello '+name

print(hello1())

#Atribua um rótulo à função. Note-se que não estamos usando parênteses aqui porque não estamos
#chamando a função hello, em vez disso, estamos apenas colocando-a em uma variável.

greet = hello1

print(greet)

print(greet())

#Essa definição não está ligada a função original:
del hello1

# hello() ira dar erro
print(greet())
print('\n')

def hello2(name='Jose'):
    print('The hello() function has been executed')
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")

hello2()
print('\n')

def hello(name='Rodrigo'):
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    if name == 'Rodrigo':
        return greet #esta retornando o endereco da funcao e nao a funcao, logo a funcao nao esta sendo executada
    else:
        return welcome

x = hello()

print(x)

# Note como x está apontando para a função greet, dentro da função hello.
print(x())

#O if/else dentro da função estão retornando greet e welcome, não greet() e welcome(). 
# Se você colocar o parêntesis acabará por executar as funções. Sem eles, é possível 
# passar os mesmos para outras variáveis.

#Quando escrevemos x = hello(), hello() é executado e o nome passado é Rodrigo, então a 
# função greet é retornada. Se mudarmos a definição para x = hello(name="Paulo") a 
# função retornada será welcome. Podemos também tentar printar hello()() que fará com que 
# a funão greet seja executada.

hello()()
print('\n')

def hello3():
    return 'Hi Jose!'

def other(func):
    print('Other code would go here')
    print(func())

other(hello3)

#Ótimo! Olhe como podemos passar funções como objetos e usá-los dentro de outras funções. Agora conseguimos construir nosso primeiro decorador:

#Criando decoradores
#No exemplo anterior nós criamos manualmete um decorador. Aqui nós iremos modificá-lo para clarificar as coisas:
print('\n')

def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator1():
    print("This function is in need of a Decorator")

func_needs_decorator1()
print('\n')

# Redefine a função
func_needs_decorator1 = new_decorator(func_needs_decorator1)

func_needs_decorator1()
print('\n')
#O que aconteceu aqui? Um simples decorador entrou na função e modificou seu comportamento. Agora vamos entender como nós podemos reescrever este código usando o simbolo @, que Python usa como decorador.

#cria o decorador direto, sem precisar passar os parametros
@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()