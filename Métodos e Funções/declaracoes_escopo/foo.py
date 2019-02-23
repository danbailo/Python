#Quando você cria um nome de variável em Python, o nome é armazenado em um namespace. 
#Nomes de variáveis também têm escopo. O escopo determina a visibilidade desse nome de
#variável para outras partes do seu código.

x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

#Em termos simples, a idéia de scope pode ser descrita por 3 regras gerais:
#As atribuições de nomes criam ou alteram nomes locais por padrão.
#Existem 4 possíveis scopes. São eles:
    #local
    #enclosing functions
    #global
    #built-in
#Os nomes declarados em declarações globais e não locais mapeiam nomes atribuídos para 
#preencher módulos e escopos de função.

# ** Regra LEGB. **
# 
# L: Local - Nomes atribuídos de qualquer forma dentro de uma função (def ou lambda)) e declarações não globais nessa função.
# 
# E: Enclosing function locals - Nome no escopo local de todas e quaisquer funções enclapsuladas (def ou lambda), de dentro para fora.
# 
# G: Global (módulo) - Nomes atribuídos no nível superior de um arquivo de módulo, ou declarados como global em uma def dentro do arquivo.
# 
# B: Built-in (Python) - Nomes pré-atribuídos no módulo: open, range, SyntaxError, ...

# x é local aqui:
f = lambda x:x**2


# Locais encapsulados em funções
# Isso ocorre quando temos uma função dentro de uma função (funções aninhadas).
name = 'This is a global name'

def greet():
    name = 'Sammy'
    
    def hello():
        print('Hello '+name)
    
    hello()

#hello() erro, dentro de outro escopo
greet()
print(name)

#Built-in
#Estes são os nomes de funções incorporados no Python (não substitua estes!)
len

#Variáveis Locais
#Quando você declara variáveis dentro de uma definição de função, elas não estão relacionadas 
# de nenhuma maneira a outras variáveis com os mesmos nomes usados fora da função 
#- ou seja, os nomes de variáveis são locais para a função. Isso é chamado de escopo da variável. 
#Todas as variáveis têm o escopo do bloco em que são declarados a partir do ponto de definição do nome.

#Exemplo:

x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)


#A declaração global
#evitar
x = 50

def funct():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
funct()
print('Value of x (outside of func()) is: ', x)

# print(locals())
# print(globals())

