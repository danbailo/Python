import heapq

class Pessoa(object):
    
    def __init__(self,nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def __repr__(self): #objeto seja impresso de forma legível
        return self.getNome()

class FilaDePrioridade(object):
    
    def __init__(self):
        self.__fila = []
        self.__indice = 0

    def inserir(self, item, prioridade):
        heapq.heappush(self.__fila, (-prioridade, self.__indice, item)) #negando a prioridade, logo se torna uma max heap, ordenado de maior prioridade para menor prioridade
        self.__indice += 1

    def remover(self):
        return heapq.heappop(self.__fila)[-1] #retorna o item(ultimo elemento da tupla) = [2]

    def show(self):
        for i in self.__fila:
            print(i)


fph = FilaDePrioridade()

fph.inserir(Pessoa('Josué'),10)
fph.inserir(Pessoa('Lucas'),15)
fph.inserir(Pessoa('Daniel'),30)
fph.inserir(Pessoa('Naul'),23)
fph.inserir(Pessoa('Lucilei'),27)

fph.show()

print(fph.remover())

fph.show()
