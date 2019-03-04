#Problema 1
#Manuseie a exceção lançada pelo código abaixo usando os blocos try e except.

for i in ['a','b','c']:
    try:
        print(i**2)
    except:
        print('Nao e possivel fazer essa operacao com string\n')
        break

#solucao do prof
try:
    for i in ['a','b','c']:
        print(i**2)        
except:
    print('erro!')


#Problema 2
#Manuseie a exceção gerada pelo código abaixo usando os blocos try e except. Em seguida, use um 
# bloco finally para imprimir 'All Done'.

x = 5
y = 0

try:
    z = x/y
except:
    print('Nao e possivel fazer divisao por zero')
    #continue so pode usar em loop
finally:
    print('All Done\n')

#Problema 3
#Escreva uma função que solicite um número inteiro e imprima o quadrado dele. Use um loop while 
#com um try, except e else para contabilizar as entradas incorretas.

def int_number():
    while True:
        try:
            number = int(input("Please enter an integer: "))
            print(number**2)
        except:
            print('Please, input a integer')
            continue
        else:
            print('Yep thats an integer!') #se nao causar excecoes(erros), roda isso
            break
        finally: #sempre vai executar
            print("I executed!") #verifica se a excecao foi tratada, caso contrario, o programa pararia a execucao

int_number()
print('\n')

def int_number2():
    while True:
        try:
            number = int(input("entre com um inteiro: "))
            print(number**2)
            break
        except:
            print('por favor, um inteiro')
            continue

int_number2()

# def test_int(x):
#     while True:
#         try:
#             if x == int(x):
#                 return print(x**2)
#             else:
#                 x = int(input())
#                 return print(x**2)
#         except:
#             print('Please, input a integer')
#             continue
#         else:
#             print('Thank you!')
#             break

# test_int(2)