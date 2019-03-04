import random

# x = ['A',2,3,4,5,6,7,8,9,10,'Q','J','K']

# random.shuffle(x)

# print(len(x))

# print([x[0]])

class Deck(object):
    def __init__(self):
        self.deck = ['A',2,3,4,5,6,7,8,9,10,'Q','J','K']
        random.shuffle(self.deck)
        pass

    def get_card(self):
        return self.deck


class Player(Deck):

    def __init__(self):
        Deck.__init__(self)
        self.wallet = float(5000)
        self.deck = [self.get_card()[0],self.get_card()[1]]
        pass

    def safe(self):
        pass
    def surrender(self):
        pass

player = Player()

print(player.deck)

# player.deck = get_card()[0]

# global teste

def test_global(teste):
    global teste = teste

# def test_print():
#     # print(teste)
# test_global()
test_global(10)
# print(teste)