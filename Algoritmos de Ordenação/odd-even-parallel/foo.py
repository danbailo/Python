#https://pt.stackoverflow.com/questions/214134/paralelizar-algoritmo-de-ordena%C3%A7%C3%A3o-odd-even-sort-em-python
from threading import Thread
import time


c_sorted = False
swaps = 0

tic = time.time()

# Função que inverte os valores se necessário:
def swap (sequence, i, j):
    global c_sorted, swaps
    if sequence[i] > sequence[j]:
        sequence[i], sequence[j] = sequence[j], sequence[i]
        c_sorted = False
        swaps += 1

# Sequência a ser ordenada:
sequence = [4,3,2,1,3,6,9,1,2,3,54,76,98,12,333,331,33,1,7,9]

# Condição se a lista está ordenada:
while not c_sorted:
    c_sorted = True
    # Lista de threads para índices pares:
    evens = []

    # Swap entre todos os valores de índice par com seu sucessor imediato:
    for i in range(0, len(sequence), 2):
        t = Thread(target=swap, args=(sequence, i, i+1))
        t.run()
        evens.append(t)

    # Aguarda todas as threads anteriores:
    (t.join() for t in evens)

    # Lista de threads para índices ímpares:
    odds = []

    # Swap entre todos os valores de índice ímpar com seu sucessor imediato:
    for i in range(1, len(sequence)-1, 2):
        t = Thread(target=swap, args=(sequence, i, i+1))
        t.run()
        odds.append(t)

    # Aguarda todas as threads anteriores:
    (t.join() for t in odds)

print(sequence)
print("swaps: %d" % swaps)
toc = time.time()

print("tempo gasto para processar = " + str(toc-tic)+"s")
