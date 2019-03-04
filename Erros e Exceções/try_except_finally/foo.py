# try e except
# A terminologia básica e a sintaxe usadas para lidar com erros no Python são as instruções
# try e except. O código que pode causar uma exceção ocorre é colocado no bloco try e o 
# tratamento da exceção é implementado no * do bloco de código except. O formulário de sintaxe é:

# try:
#    Você tenta fazer algo aqui...
#    ...
# except ExceptionI:
#    Se causar a ExceptionI, roda isso.
# except ExceptionII:
#    Se causar a ExceptionII, roda isso.
#    ...
# else:
#     Se não causar excessões, roda isso.

#https://docs.python.org/2/library/exceptions.html

#Nós também podemos apenas verificar qualquer exceção apenas com except: Para obter uma melhor 
# compreensão de tudo isso, vamos verificar um exemplo: Vamos ver algum código que abre e grava 
# um arquivo:

try:
    f = open('testfile.txt','w')
    f.write('Test write this')
except IOError:
    # Isso só irá verificar se há uma exceção IOError e, em seguida, executar esta declaração de impressão
   print("Error: Could not find file or read data")
else:# se nao houver nenhum erro, o else sera executado!
   print("Content written successfully")
   f.close()

try:
    f = open('testfile.txt','r')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
   print("Error: Could not find file or read data")
else:
   print("Content written successfully")
   f.close()

#Ótimo! Observe como imprimimos apenas uma declaração! O código ainda correu e conseguimos 
# continuar fazendo ações e executando blocos de código. Isso é extremamente útil quando você 
# deve ter em conta possíveis erros de entrada em seu código. Você pode estar preparado para o 
# erro e continuar executando o código, em vez de seu código apenas quebrar como vimos acima.

#Também poderíamos ter imprimido caso não tivéssemos certeza de qual seria a exceção. Por exemplo:

try:
    f = open('testfile','r')
    f.write('Test write this')
except:
   print("Error: Could not find file or read data")
else:
   print("Content written successfully")
   f.close()

#Ótimo! Agora, na verdade, não precisamos memorizar essa lista de tipos de exceção! 
# Agora, e se continuássemos querendo executar código após a ocorrência da exceção? 
# É aí que o finally entra.

# finally
# O finally: o bloco de código sempre será executado, independentemente de existir uma exceção 
# no bloco de código try. A sintaxe é:

# try:
#    Seu código aqui
#    ...
#    Devido a qualquer exceção, este código pode ser ignorado!
# finally:
#    Este bloco de código sempre seria executado.
# Por exemplo:

try:
   f = open("testfile.txt", "w")
   f.write("Test write statement")
finally:
   print("Always execute finally code blocks")

#Nós podemos usar finally em conjunto com except. Vamos ver um novo exemplo que levará em 
# consideração um usuário que coloque a entrada errada:

# def askint():
#         try:
#             val = int(raw_input("Entre um inteiro: "))
#         except:
#             print("Parece que você não digitou um inteiro")
            
#         finally:
#             print("Executei!")
#         print(val)       

# askint()

#Observe como obtivemos um erro ao tentar imprimir val (porque nunca foi atribuído corretamente). 
# Repare isso perguntando ao usuário e verificando se o tipo de entrada é um número inteiro:

#Como podemos continuar continuando a verificar? Podemos usar um loop while!

def askint1():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print('Yep thats an integer!')
            break
        finally:
            print("Finally, I executed!")
        print(val) 

askint1()