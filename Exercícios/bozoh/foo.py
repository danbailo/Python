import random

dice = [1, 2, 3, 4, 5, 6]

class Player:
    def __init__(self, name):
        self.name = name
        # self.points = [['as','fu','sena'],['duque','seq','quarta'],['3',3,3],[4,4,4]]
        self.points = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]

    def getname(self):
        return self.name

    def makemove(self):
        global dice
        random.choice(dice)

    def addpoints(self):
        pass

def showpoints(matrix):
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print('')

p1 = Player("Daniel")

print(p1.getname())
# print(p1.points)

showpoints(p1.points)