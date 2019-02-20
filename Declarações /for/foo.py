l = [1,2,3,4,5,6,7]

# for i in x
# nesse caso o i vale 0, pois nao foi atribuido nenhum valor antes do for
# se n tiver nada, atribui o primeiro valor a ser setado para ele como o primeiro

#o num é uma variavel declarada e pode ser qqr nome
for num in l:
    print('num vezes 1:',num)
    print('num vezes 2:',num*2)
    print('num vezes 3:',num*3)

#verificar os pares
for num in l:
    if num % 2 == 0:
        print('Par:',num)
    else:
        print('Ímpar:',num)

#somatario
soma = 0
for num in l:
    soma += num

print(soma)

#string
string = 'essa e uma string'
for char in string:
    if char == 'e':
        print(char)

#tupla
tupla = (1,2,5,4,7)

for tup in tupla:
    print(tup)


#desembalagem de tupla
l = [(1,2),(2,3),(3,4)]
print(l[1])

(t1,t2) = l[0]
print(t1,t2)

for (t1,t2) in l:
    print(t1*t2)

#dicionario

d = {
    'key1':1,
    'key2':2,
    'key3':3
}

print(d)

for key in d:
    print(key)

for value in d.values():
    print(value)

for (key,value) in d.items():
    print(value)