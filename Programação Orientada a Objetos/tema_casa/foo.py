#Problema 1
#Preencha os métodos da classe Line para aceitar coordenadas como um par de tuplas e retornar 
# a inclinação e a distância da linha.

import math

class Line(object):
    #o nome da variavel utilizada no parametro e ilutrativo, pois o nome usado nos metodos é o 
    #que foi passado na instancia da classe;
    def __init__(self,coord1,coord2): 
        self.coord1 = coord1
        self.coord2 = coord2
    
    def distance(self):
        # x1,y1 = self.coor1 se eu quiser tirar os "self"
        # x2,y2 = self.coor2
        # raiz é mesma coisa que **0.5
        return math.sqrt((self.coord2[0]-self.coord1[0])**2+(self.coord2[1]-self.coord1[1])**2)
    
    def slope(self):
        return (self.coord2[1]-self.coord1[1])/(self.coord2[0]-self.coord1[0])

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())
print(li.slope())

#Problema 2
#Preencha a classe

class Cylinder(object):
    
    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.pi*self.radius**2*self.height
    
    def surface_area(self):
        return 2*self.pi*self.radius**2+2*self.pi*self.radius*self.height

# Exemplo de saída
c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())