#Embaralhar cartas
import random

playing = False
chip_pool = 100

bet = 1

restart_phrase = 'Press "d" to shuffle again or press "q" to leave'

ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K')

card_val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Q':10, 'J':10, 'K':10}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.suit + self.rank
    
    def grab_suit(self):
        return self.suit
    
    def grab_rank(self):
        return self.rank
    
    def draw(self):
        print (self.suit + self.rank)

class Hand(object): #conjunto de cartas
    def __init__(self):
        self.cards = [] #cria uma lista vazia, mas essa variavel recebera varios objetos do tipo card
        self.value = 0 #inicialmente é 0, mas o valor vai aumentando a medida q vamos adicionando cartas na mao
        self.ace = False #define se a mao tem ou nao um ace(ace=ás)
    def __str__(self):
        hand_comp = ""#vazio/composição da mao

        for card in self.cards:
            card_name = card.__str__()
            hand_comp += " " + card_name

        return "The hand has {}".format(hand_comp)

    def card_add(self, card):
        self.cards.append(card)

        if card.rank == 'A':
            self.ace = True
        self.value += card_val[card.rank] #acessando o rank/value do dicionario para adicionar no valor da mao

    def calc_val(self): 
        if (self.ace == True and self.value < 12):
            return self.value + 10
        else:
            return self.value

    def draw(self,hidden):
        if hidden == True and playing == True:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
            self.cards[x].draw() #printar as cartas da mao, exceto pela primeira carta se hidden = true

class Deck(object):
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += " " + card.__str__()
        return 'The deck has '+deck_comp

#aposta
def make_bet():
    global bet
    bet = 0

    print('What amount of chips you like to bet? (Enter whole integer please)')

    while bet == 0:
        bet_comp = int(input())

        if bet_comp >= 1 and bet_comp <= chip_pool:
            bet = bet_comp
        else:
            print('Invalid bet. You have only '+str(chip_pool)+'chips remaing.')

def deal_cards():
    global result, playing, deck, player_hand, dealer_hand, chip_pool, bet

    deck = Deck()
    deck.shuffle()

    make_bet()

    player_hand = Hand()
    dealer_hand = Hand()

    # 2 cards for Player
    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

    # 2 cards for Dlayer
    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    result = 'Hit or Stand? Press "h" or "s": '

    chip_pool -= bet

    playing = True
    game_step()

def hit():
    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

    if playing:
        if player_hand.value() <= 21:
            player_hand.card_add(deck.deal())
        print('Player hand is %s'%player_hand)

        if player_hand.value() > 21:
            result = 'Busted! ' + restart_phrase
            chip_pool -= bet
            playing = False
    else:
        result = "Sorry, can't hit! " + restart_phrase

def stand():
    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

    if playing == False:
        if player_hand.calc_val() > 0:
            result = "Sorry, you can't stand!"

    else:
        while dealer_hand.calc_val() < 17:
            dealer_hand.card_add(deck.deal())
        
        if dealer_hand.calc_val() > 21:
            result = 'Dealer busts! You win!' + restart_phrase
            chip_pool += bet
            playing = False

        elif dealer_hand.calc_val() < player_hand.calc_val():
            result = 'You beat the dealer! You win!' + restart_phrase
            chip_pool += bet
            playing = False

        elif dealer_hand.calc_val() == player_hand.calc_val():
            result = 'Tied up! You win!' + restart_phrase
            playing = False

        else:
            result = 'Dealer wins! ' + restart_phrase
            chip_pool -= bet
            playing = False
    game_step()

def game_step(): # a cada decisao
    print('')
    print(' Player hand is:')
    player_hand.draw(hidden=False)
    print('Player hand total is: ' + str(player_hand.calc_val()))

    print('')
    print(' Dealer hand is:')
    dealer_hand.draw(hidden=True)
    print('Dealer hand total is: ' + str(dealer_hand.calc_val()))

    if playing == False:
        print('Chip total: '+str(chip_pool))

    print(result)

    player_input()

def game_exit():
    print('Thanks for playing!')
    exit()

def player_input():
    plin = input().lower

    if plin == 'h':
        hit()
    elif plin == 's':
        stand()
    elif plin == 'd':
        deal_cards()
    elif plin == 'q':
        game_exit()
    else:
        print('Invalid input! Enter h,s,d or q: ')
        player_input()

def intro():
    statement = '''\nWelcome to BlackJack! Get as close to 21 as you can without going over!
Dealer hits until she reaches 17. Aces count as 1 or 11.Card output goes a letter 
followed by a number of face notation
        '''
    print(statement)

deck = Deck()
deck.shuffle()

player_hand = Hand()
dealer_hand = Hand()

intro()
deal_cards()