#diferença de um iterável normal para um gerador, é q o iteravel carrega tudo na memoria
#de uma vez, e o gerador nao

def gencubes(n):
    for num in range(n):
        yield num**3 #return da erro

for x in gencubes(10):
    print(x)

#equivalente usando iteravel
def gencubes2(n):
    lst = []
    for num in range(n):
        lst += [num**3]
    return lst

for x in gencubes2(10):
    print(x)

print('\nFibonnaci')
def fibonacci(number):
    a = 0
    b = 1
    for n in range(0,number):
        yield a
        a, b = b, a+b


for x in fibonacci(15):
    print(x)

def fibonacci2(number):
    a = 0
    b = 1
    output = []
    for n in range(0,number):
        output += [a]
        a, b = b, a+b
    return output

for x in fibonacci2(15):
    print(x)

print(list(fibonacci(15)))
print(fibonacci2(15))

g = fibonacci(5) #funcao geradora

print(next(g)) #
print(next(g)) #
print(next(g)) #
print(next(g)) #
print(next(g)) #5 primeiros valores
# print(next(g)) #error

s = 'Hello'

for char in s:
    print(char)

#next(s) # nao e iterador

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
# print(next(s_iter))
# print(next(s_iter))