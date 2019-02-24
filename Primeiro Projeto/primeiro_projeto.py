import random
from IPython.display import clear_output
def display_board(board):
    clear_output()
    for index, item in enumerate(board, start=0):
        print(item, end=' | ' if index % 3 else '\n')

def player_input():   
    marker = ''
    
    #enquanto nao for igual, repita
    while not (marker == 'X' or marker == 'O'): #forca o usuario a digitar "X" ou "O"
        marker = str(input('Player 1: Você quer ser X ou O? ')).upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    return( (board[1] == mark and board[2] == mark and board[3] == mark) or #primeira linha
            (board[4] == mark and board[5] == mark and board[6] == mark) or #segunda linha
            (board[7] == mark and board[8] == mark and board[9] == mark) or #terceira linha
            (board[1] == mark and board[5] == mark and board[9] == mark) or #diagonal
            (board[3] == mark and board[5] == mark and board[7] == mark) or #diagonal
            (board[1] == mark and board[4] == mark and board[7] == mark) or #primeira coluna
            (board[2] == mark and board[5] == mark and board[8] == mark) or #segunda coluna
            (board[3] == mark and board[6] == mark and board[9] == mark)    #terceira coluna
            )

def choose_first():
    if random.randint(0,1) == 0: #gera um numero aleatorio no intervalo de 0 a 1
        return('Player 1')
    else:
        return('Player 2')

def space_check(board,position):
    return board[position] == ' ' #se estiver vazio, ele retorna TRUE

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i): #logo, se estiver algum espaco vazio, ele retorna True,
            return False #entra no if e a funcao tem valor de False
        
    return True #caso nenhum espaco esteja vazio, ele nunca ira entrar no if, entao retorna 
                #True para confirmar q a board esta cheia

def player_choice(board):
    position = ' ' #espaco em branco != '' isso é nada

    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = str(input('\nEscolha sua jogada (1-9): ')) #forca o usuario a digitar os numeros
                                                            #de 1 a 9, e sem repeticao!
    return int(position)

def replay(): #retorna true caso uma palavra com a digital S seja entrada
    return str(input('Quer jogar novamente? "Sim" ou "Não": \n')).lower().startswith('s')

def main():
    print('Bem vindo ao Jogo da Velha')

    while True:
        board = [' '] * 10 #[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 0 a 9
        player1_marker,player2_marker = player_input()
        turn = choose_first()
        print(turn+' começa!')

        game_on = True

        while game_on:
            #vez do jogador 1
            if turn == 'Player 1':
                display_board(board)
                position = player_choice(board)
                place_marker(board, player1_marker, position)

            # checa vitória
            if win_check(board, player1_marker):
                display_board(board)
                print('\nParabéns Jogador 1, você ganhou!\n')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('\nEmpate!\n')
                    break
                else:
                    turn = 'Player 2'

            #vez do jogador 2
            if turn == 'Player 2':
                display_board(board)
                position = player_choice(board)
                place_marker(board, player2_marker, position)

            # checa vitória
            if win_check(board, player2_marker):
                display_board(board)
                print('\nParabéns Jogador 2, você ganhou!\n')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('\nEmpate!\n')
                    break
                else:
                    turn = 'Player 1'

        #se digitado qqr coisa diferente de sim, ele ira retornar true, mas como o not inverte o valor logico
        #ele entra no if e para o programa
        if not replay():
            break

if __name__ == '__main__':
    main()