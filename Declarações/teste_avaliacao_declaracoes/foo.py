#Use for, split() e if para criar uma declaração que imprima as palavras que começam com 's':

st = 'Print only the words that start with s in this sentence'

string = st.split() #quebra a string numa lista, a cada espaço

print(string)

for letter in string:
    if letter[0] == 's':
        print(letter)
print('\n')
#** Use range() para imprimir todos os números pares de 0 a 10. **

for i in range(10):
    if i%2==0:
        print(i)
print('\n')

#** Use a compreensão de lista para criar uma lista de todos os números entre 1 e 50 que 
# são divisíveis por 3. **

x = [i for i in range(50) if i%3==0]
print(x)
print('\n')

#** Percorra a string abaixo e se o comprimento de uma palavra for par imprima "é par!" **
st = 'Print every word in this sentence that has an even number of letters'

string = st.split() #quebra a string numa lista, a cada espaço

for word in string:
    if len(word)%2==0:
        print(word, 'é par e tem {} letras'.format(len(word)))
print('\n')

#** Escreva um programa que imprima os números inteiros de 1 a 100. Para múltiplos de 
# três imprima "Fizz" ao invés do número, e para os múltiplos de cinco imprima "Buzz". 
# Para números que são múltiplos de três e cinco imprima "FizzBuzz". **

for i in range(101):
    if (i%3==0 and i%5==0): #sempre colocar o com mais incidencias possiveis mais acima
        i= 'FizzBuzz'       #para garantir exclusividade
    elif i%3==0:
        i = 'Fizz'
    elif i%5==0:
        i = 'Buzz'
    print(i)
print('\n')

#** Use Compreensão em listas para criar uma lista das primeiras letras de cada palavra na 
# string abaixo: **

st = 'Create a list of the first letters of every word in this string'
string = st.split()

char = [c[0] for c in string]

print(char)