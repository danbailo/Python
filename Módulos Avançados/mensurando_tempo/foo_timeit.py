#Medindo o tempo do seu código
# Às vezes, é importante saber em quanto tempo o seu código está sendo executado ou, 
# pelo menos, saber se uma determinada linha de código está trancando seu projeto inteiro. 
# O Python possui um módulo de temporização incorporado para fazer isso.
#
# Este módulo fornece uma maneira simples para o medir o tempo de pequenos bits do código Python.
# Possui tanto uma interface de linha de comando quanto uma chamada. Ele evita várias armadilhas
# comuns para medir os tempos de execução.
# 
# Vamos aprender sobre o timeit!

import timeit

#Permite usar timeit para medir a eficiência de vários métodos para criar a string '0-1-2-3 -.....- 99'

#Passaremos dois argumentos: a linha real que queremos testar encapsulada como uma string e o 
# número de vezes que desejamos executá-la. Aqui escolheremos 10.000 corridas para obter alguns
# números suficientemente altos para comparar vários métodos.

# For

print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))#para saber em 1, basta dividir o resultado por 10000

# Compreensão em listas
print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))

# Map()
print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))