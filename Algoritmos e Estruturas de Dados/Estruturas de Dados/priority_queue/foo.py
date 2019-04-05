class Person(object):
    def __init__(self,name,prior):
        self.__name = name
        self.__prior = prior
    
    def getName(self):
        return self.__name

    def getPrior(self):
        return self.__prior

class PriorityQueue:
    def __init__(self):
        self.__pq = []
        self.__len = 0

    #insere decrescentemente pela prioridade
    def push(self, person):
        if self.empty():
            self.__pq.append(person)
        else:
            flag_push = False
            
            for i in range(self.__len): #procura onde inserir para manter a fila ordenada
                if self.__pq[i].getPrior() < person.getPrior():
                    self.__pq.insert(i,person)
                    flag_push = True
                    break
            
            if not flag_push: #se entrou aq e pq vai inserir no final
                self.__pq.insert(self.__len, person)
        
        self.__len += 1 
    
    def pop(self):
        if not self.empty():
            self.__pq.pop(0)
            self.__len -= 1

    def empty(self):
        if self.__len == 0:
            return True
        return False

    def show(self):
        for p in self.__pq:
            print('Name "%s"'%p.getName(), end = ', ')
            print('Priority "%d"'%p.getPrior())
        
#objetos
p1 = Person('Daniel',20)
p2 = Person('Lucas',3)
p3 = Person('Josué',7)
p4 = Person('Naul',12)
p5 = Person('Lucilei',67)

#fila
pq = PriorityQueue()

pq.push(p1)
pq.push(p2)
pq.push(p3)
pq.push(p4)
pq.push(p5)

pq.show()

pq.pop()
print('\n')
pq.show()

pq.pop()
print('\n')
pq.show()

print('\n')
pq.push(Person('Goku',58))
pq.show()

print('\n')
pq.push(Person('asdas',9))
pq.show()

print('\n')
pq.push(Person('asdas',1))
pq.show()

print('\n')
pq.push(Person('asdas',2))
pq.show()


