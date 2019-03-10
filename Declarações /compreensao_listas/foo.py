#criando uma lista grande
# x = [1,2,3,4...] -> nao recomendado

#uma maneira
x = []

for i in range(10):
    x.append(i)
    #x =x+[i] #concatenando uma lista
print(x)
del x
print('\n')

#outra maneira
x = [i for i in range(10,20)]
print(x)
del x
print('\n')

####

x = [i*2+10 for i in range(15)]
print(x)
del x
print('\n')

###

x = []
for i in range (20):
    if i%2 == 0:
        x += [i]
        #x.append(i)
print(x)
del x
print('\n')

###

x = [i for i in range(20) if i%2 == 0]
print(x)
del x
print('\n')

###

lista = []
for letter in 'word':
    lista.append(letter)

print(lista)
del lista
print('\n')

lista = [letter for letter in 'word']
print(lista)
del lista
print('\n')

###

#celsius para fahrenheit

celsius = [0, 10, 15, 20, 30, 50, 100]

fahrenheit = [(temp*1.8)+32 for temp in celsius]

print(celsius)
print(fahrenheit)
print('\n')

#lista aninhada
lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst)


print("\ni'm here")

x = [[] for i in range(3)]

print(x)