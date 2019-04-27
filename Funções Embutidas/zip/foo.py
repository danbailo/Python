#zip condensa 2 iteraveis juntos

x = [2, 3, 4, 6, 7, 8]
y = [4, 1, 8, 2, 9, 11]

print(list(zip(x,y))) #retorna uma lista de tuplas

for i in zip(x,y):
    print(i)

for i in zip(x,y):
    print(max(i)) #printa o maior valor da tupla

a = [1, 2, 3, 4]
b = [8, 9]

#neste caso ele retorna o tamanho da menor lista
print(list(zip(a,b)))



d1 = {'key5':2,'key4':5}
d2 = {'key1':8,'key2':9}

#retorna somente as keys
print(list(zip(d1, d2)))

print(list(zip(d1, d2.values() )))
