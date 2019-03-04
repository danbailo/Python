import random
class Card(object):
    def __init__(self,no,naipe):
        self.no=no
        self.naipe=naipe
    def __str__(self):
        no=""
        if self.no==1:
            no="A"
        elif self.no==10:
            no="J"
        elif self.no==11:
            no="Q"
        elif self.no==12:
            no="K"
        else:
            no=str(self.no)
        return no+" "+self.naipe
class Player(object):
    def __init__(self):
        self._deck=[]
    def insertCard(self,card):
        self._deck.append(card)
    def print(self):
        if(len(self._deck)==0):print("Vazio")
        for card in self._deck:
            print(card)
    def countBJ(self):
        ans=0
        for card in self._deck:
            if card.no>10:
                ans+=10
            else:
                ans+=card.no
        return ans
class Dealer(object):
    def __init__(self):
        self._deck=[]
        naipes=["♦","♠","♥","♣"]
        for j in naipes:
            for i in range(1,13):
                self._deck.append(Card(i,j))
        random.shuffle(self._deck)
    def deal(self):
        return self._deck.pop()
   
d=Dealer()
p=Player()
while True:
    bj=p.countBJ()
    print("--------------")
    print("Cartas")
    p.print()
    print("--------------")
    print("Contagem cartas")
    print(p.countBJ())
    print("--------------")
    if bj==21:
        print("Ganhou!!")
        break
    elif bj>21:
        print("Estorou")
        break
    print("Comprar?:")
    u=input()
    if u=="s":
        c=d.deal()
        print("carta é:")
        print(c)
        p.insertCard(c)
        print("--------------")
    elif u=="n":
        print("fim de jogo")
        print("--------------")
        print("Cartas")
        p.print()
        print("--------------")
        print("Contagem cartas")
        print(p.countBJ())
        print("--------------")
