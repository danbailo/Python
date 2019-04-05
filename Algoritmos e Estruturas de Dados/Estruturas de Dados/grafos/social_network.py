from collections import defaultdict

class Person:
    def __init__(self, name, age):
        self.name = name        
        self.age = age        

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    # def __str__(self):
    #     return 'name: {}, age: {}'.format(self.getName(),self.getAge())

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEgde(self, p1, p2):
        self.graph[p1.getName()].append(p2)
        self.graph[p2.getName()].append(p1)

    def showFriends(self, person):
        for v in self.graph[person.getName()]:
            print('Friendship of {} is {}'.format(person.getName(),v.getName()))
        print('')

g = Graph()

p1 = Person('Daniel', 19)
p2 = Person('Josue', 19)
p3 = Person('Lucas', 22)
p4 = Person('Naul', 51)
p5 = Person('Lucilei', 44)

g.addEgde(p1,p2)
g.addEgde(p1,p3)
g.addEgde(p1,p4)
g.addEgde(p1,p5)

g.addEgde(p2,p4)
g.addEgde(p2,p5)

g.showFriends(p1)
g.showFriends(p2)
g.showFriends(p3)
g.showFriends(p4)
g.showFriends(p5)
