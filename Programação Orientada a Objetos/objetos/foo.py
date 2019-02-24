#Resumo de forma geral

#Classes
# Uma classe é uma estrutura que abstrai um conjunto de objetos com características similares. 
# Uma classe define o comportamento de seus objetos - através de métodos - e os estados possíveis 
# destes objetos - através de atributos.
# Em outras palavras, uma classe descreve os serviços oferecidos por seus objetos e quais 
# informações eles podem armazenar.
# Uma classe representa um conjunto de objetos com características afins. Uma classe define o 
# comportamento dos objetos através de seus métodos, e quais estados ele é capaz de manter 
# através de seus atributos.

#Objetos
# Um objeto, na vida real, é qualquer coisa a qual pudermos dar um nome.
# Um objeto, em programação orientada a objetos, é uma instância (ou seja, um exemplar) de uma 
# classe. A Wikilivros é um exemplo de Wiki, ou, a Wikilivros é uma instância de Wiki. 
# Isto poderia ser representado em um programa orientado a objetos com uma classe chamada 
# Wiki e um objeto do tipo Wiki chamado Wikilivros.
# Um objeto é capaz de armazenar estados através de seus atributos e reagir a mensagens enviadas
# a ele, assim como se relacionar e enviar mensagens a outros objetos.
# Atributos são características de um objeto. Basicamente a estrutura de dados que vai 
# representar a classe.
# Exemplos: um objeto da classe "Funcionário" teria como atributos "nome", "endereço", 
# "telefone", "CPF", etc.
# O conjunto de valores dos atributos de um determinado objeto é chamado de estado.

#Em Python, tudo é um objeto. 
#Os objetos definidos pelo usuário são criados usando a palavra-chave da class.A classe é um 
# modelo que define a natureza de um objeto futuro. Das classes podemos construir instâncias. 
# Uma instância é um objeto específico criado a partir de uma determinada classe. 
# Por exemplo, acima, criamos o objeto 'l' que era uma instância de um objeto da classe lista.

# Crie um novo tipo de objeto chamado Sample
class Sample(object): #por padrao do python, logo, se essa classe n herdar ninguem, ela é a primogenita e recebe object como parametro
    pass

# Instanciando Sample, criando um obj que tem o tipo da classe que eu criei
x = Sample()

print(type(x))

#Por convenção damos às classes um nome que começa com uma letra maiúscula. Observe como x 
# é agora a referência para nossa nova instância da classe Sample. Em outras palavras, nós 
# instanciamos a classe Sample.
#Dentro da classe temos apenas um pass. Mas podemos definir atributos e métodos de classe.

#Um atributo é uma característica de um objeto. Um método é uma operação que podemos realizar com o objeto.

#Por exemplo, podemos criar uma classe chamada Dog. Um atributo de Dog pode ser sua raça ou seu 
# nome, enquanto um método de um cão pode ser definido por um método .latir() que retorna um som.
#Vamos ter uma melhor compreensão dos atributos através de um exemplo.

#Atributos->variaveis que vivem dentro de classes
#A sintaxe para criar um atributo é:

#self.attribute = something
#Existe um método especial chamado:

#Nisso
#__init__() -> Construtuor
#primeiro parametro de um construtor em python, "sempre" sera __init__(self,), pois assim
#o python vai saber que estamos nos referenciando a esta classe

#Esse método é usado para inicializar os atributos de um objeto. Por exemplo:

class Dog(object):
    def __init__(self,raça): #o python procura a __init__(), q é a funcao de inicializacao de classes
        self.raça = raça     # no caso, seria o "CONSTRUTOR" em python!        
        #a raça do parametro interno da classe, ira receber a raca que foi passado como parametro no construtor

bernardo = Dog('spitz')
sam = Dog(raça='Lab')
frank = Dog(raça='Huskie')

#Vamos descrever o que temos acima. O método especial
# 
#  __init__()
# é chamado automaticamente logo após o objeto ter sido criado:
# 
#  def __init __(self, raça):
# Cada atributo em uma definição de classe começa com uma referência ao objeto de instância. 
# É convencionalmente chamado de self. A raça é o argumento. O valor é passado durante a 
# instanciação da classe.
# 
#   self.breed = breed

#Agora criamos duas instâncias da classe Dog. Com dois tipos de raças, podemos acessar estes atributos assim:

print(sam.raça)
print(frank.raça)
print(bernardo.raça)

print('\n')
#Observe como não temos parênteses após a raça, isto é porque é um atributo e não leva nenhum argumento.

#Em Python também existem atributos de objeto de classe. Esses atributos de objeto de classe 
# são os mesmos para qualquer instância da classe. Por exemplo, podemos criar o atributo especie 
# para a classe Dog. Os cães (independentemente da sua raça, nome ou outros atributos 
# serão sempre mamíferos. Aplicamos essa lógica da seguinte maneira:

class Cachorro(object):
    
    # Atributos de objetos de classe
    species = 'mammal'
    
    def __init__(self,raça,nome):
        self.raça = raça
        self.nome = nome

dog1 = Cachorro('Lab','Sam')

print(dog1.raça)
print(dog1.nome)

#Note that the Class Object Attribute is defined outside of any methods in the class. 
# Also by convention, we place them first before the init.
print(dog1.species)

#Métodos
#Métodos são funções definidos dentro do corpo de uma classe. Eles são usados para executar 
# operações com os atributos de nossos objetos. Os métodos são essenciais no conceito de 
# encapsulamento em OOP. Isso é essencial para dividir as responsabilidades na programação, 
# especialmente em grandes aplicações.

#Você pode basicamente pensar em métodos como funções que atuam em um Objeto que levam o próprio 
#Objeto através de seu argumento * self *.

#Vamos passar por um exemplo de criação de uma classe Circle:

class Circle(object):
    pi = 3.14

    # O círculo é instanciado com um raio (o padrão é 1)
    def __init__(self, radius=1):
        self.radius = radius 

    # Método de cálculo da área. Observe o uso de si mesmo.
    def area(self):
        return self.radius * self.radius * Circle.pi

    # Método que redefine a área
    def setRadius(self, radius): #para todas as funcoes internas de uma classe, é preciso passar o self
        self.radius = radius

    # Método para obter raio (Mesmo que apenas chamar .radius)
    def getRadius(self):
        return self.radius


c = Circle()

c.setRadius(2) #se eu comentar essa linha, ele ira atribuir 1, como padrao
print('O raio é :',c.getRadius())
print('A área é',c.area())

print('\n')

#Ótimo! Observe como nós usamos a notação self. para atributos de referência da classe dentro 
# das chamadas do método. Revise como o código acima funciona e tente criar seu próprio método

#Herança
#A herança é uma forma de formar novas classes usando classes que já foram definidas. As classes 
# recém formadas são chamadas classes derivadas, as classes de que derivamos são chamadas de 
# classes base. Os benefícios importantes da herança são a reutilização de códigos e a redução 
# da complexidade de um programa. As classes derivadas (descendentes) substituem ou estendem a 
# funcionalidade das classes base (ancestrais).

#Vejamos um exemplo incorporando nosso trabalho anterior na classe Dog:

class Animal(object):

    x = 10

    def __init__(self): #recebe assim é que criado
        print("Animal created") 

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog2(Animal): #esse parametro q é de fato a herança
    def __init__(self): #recebe assim é que criado
        Animal.__init__(self) #se comentado tb funciona
        print("Dog created") 
        pass

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog2()

d.whoAmI()
d.eat()
d.bark()

print(d.x)

print('\n')
#Neste exemplo, temos duas classes: Animal e Dog. O animal é a classe base, o cão é a classe derivada.
# classe derivada herda a funcionalidade da classe base.
# É mostrado pelo método eat().

# A classe derivada modifica o comportamento existente da classe base.
# mostrado pelo método whoAmI().
# Finalmente, a classe derivada estende a funcionalidade da classe base, definindo um novo método de bark().

#Métodos especiais
#Finalmente, vamos dar uma olhada em métodos especiais. Classes em Python podem implementar 
# determinadas operações com nomes de métodos especiais. Esses métodos não são realmente 
# chamados diretamente, mas pela sintaxe de linguagem específica de Python. Por exemplo, 
# crie uma classe de livro:

class Book(object):
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self): #referente ao print
        return "Title:%s, author:%s, pages:%s " %(self.title, self.author, self.pages)

    def __len__(self): #referente ao len/tamanho
        return self.pages

    def __del__(self): #quando deleta o objeto
        print("A book is destroyed")

book = Book("Python Rocks!", "Rodrigo Tadewald", 159)

# Métodos especiais
print(book)
print(len(book))
del book

#Os métodos __init __(), __str __(), __len __() e __del __(). Esses métodos especiais são 
# definidos pelo uso de sublinhados. Eles nos permitem usar funções específicas do Python em 
# objetos criados através da nossa classe.