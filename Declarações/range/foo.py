#range() nos permite criar uma lista de números que variam de um ponto de partida até um ponto
# final. Também podemos especificar o tamanho do passo. 

#Para uma explicação simplificada: um gerador permite a geração de objetos gerados que são 
#fornecidos naquela instância, mas não armazena cada instância gerada na memória.

#Isso significa que um gerador não criaria uma lista ao gerar um range(), mas, em vez disso, 
#fornece uma geração única dos números nesse intervalo. A boa notítica é que range() se 
#comporta como um gerador e você não precisa se preocupar com isso.

x = range(10) #range(0,10,1)
print(x)

print(list(x))

for i in range(10): #se eu colocar so um parametro, ele reconhece como o final e
    print(i)        # atribui 0 para o i

print('\n')

for i in range(0,15): #se eu colocar dois parametros, ele identifica o inicio e o fim
    print(i)

print('\n')

for i in range(0,10,2): #se eu colocar tres parametros, ele identifica o inicio e o fim
    print(i)            #e o passo