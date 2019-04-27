#all
#retorna true se todos os elementos do iteravel for true

lst = [1, 1, 1, 1]
print(all(lst))

lst = [True, True, True, True]
print(all(lst))


lst = [True, False, True, True]
print(all(lst))

lst = [1, 1, 0, 1]
print(all(lst))

#any
#retorna true se pelo menos um elemento do iteravel for true
lst = [0, 0, 1, 0]
print(any(lst))

lst = [0, 0, 0, 0]
print(any(lst))

lst = [False, False, False, True]
print(any(lst))

lst = [False, False, False, False]
print(any(lst))

