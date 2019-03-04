import random

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
        self.deck = [self.get_card(),self.get_card()]
        pass

    def safe(self):
        pass
    def surrender(self):
        pass

class Dealer(object):
    
    pack = ['A',2,3,4,5,6,7,8,9,10,'Q','J','K']
    random.shuffle(pack)
    
    def __init__(self):
        self.cards = [self.pack[random.randint(0,12)]]     

def start_game(player,dealer):
    print('\nBeat the dealer!')
    print('The game started')
    print('\nYou have U$ {}\n'.format(player.wallet))
    print('Player cards: {}'.format(player.cards))
    print('Dealer cards: {}'.format(dealer.cards))

def hit(player):
    player.deck
    pass

def gaming(player):
    print('(1) Hit')
    print('(2) Stand')
    if int(input()) == 1:
        hit(player)
    elif int(input()) == 2:
        pass



def main():
    player = Player()
    dealer = Dealer()
    while True:
        print('\nBlackjack')
        print('(1) Start game')
        print('(2) Quit')
        try:
            option = int(input('Select a option: '))
        except:
            print('Please, input a number!\n')
            continue

        if option == 1:
            start_game(player,dealer)
            gaming(player)
        elif option == 2:
            break
    


if __name__ == "__main__":
    main()
    pass


