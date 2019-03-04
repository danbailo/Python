ranks = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']
suits = ['♣', '♦', '♥', '♠']
deck = []

class Card(object):
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    
    #se eu nao definir isso, ira printar o endereço de memoria do objeto
    def __str__(self):
        return self.rank + self.suit

class Deck(object):
    def __init__(self):
        self.deck = deck
        for rank in ranks:
            for suit in suits:
                deck.append(Card(rank,suit))
    
    #isso aqui só iria printar o endereço de memoria onde estao os objetos
    # def __str__(self):
    #     return str(self.deck)
    def __str__(self):
        deck_comp = "" #cria uma variavel string vazia
        for card in self.deck:
            deck_comp += " " + card.__str__()#card.__str__() isso aqui seria um A♣ por ex
        return deck_comp    

print(Deck())