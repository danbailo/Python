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
        self.__fila = [] #esse seria o array
        self.__indice = 0 #esse indice ordena os itens com o mesmo nivel de prioridade 

    def inserir(self, item, prioridade):
        heapq.heappush(self.__fila, (-prioridade, self.__indice, item)) #negando a prioridade, logo se torna uma max heap, ordenado de maior prioridade para menor prioridade
        self.__indice += 1

    def remover(self):
        return heapq.heappop(self.__fila)[-1] #esse indice só serve para retornar o "nome" da pessoa removida, visto que ele remove a tupla inteira, o ultimo elemento
        # da tupla é o item, que seria o nome;

    def show(self):
        for i in self.__fila:
            print(i)

    def print_array(self):
        print(self.__fila)


#A PRIORIDADE SERÁ A IDADE

#As idades printarao negativo, pois na insercao eu neguei a mesma, porem, assim,
#ela se tornou uma max heap(é o inverso da minheap, na minheap, os valores menores
# viram primeiro, mas como é tudo negativo, o maior valor negativo, é na vdd o menor valor
# entao ele vem a frente)

fph = FilaDePrioridade()

fph.inserir(Pessoa('Josué'),19)
fph.inserir(Pessoa('Lucas'),22)
fph.inserir(Pessoa('Daniel'),19)
fph.inserir(Pessoa('Naul'),51)
fph.inserir(Pessoa('Lucilei'),45)

# fph.show()
fph.print_array()

print(fph.remover())

fph.print_array()
# fph.show()

lst = [1,2,3]
