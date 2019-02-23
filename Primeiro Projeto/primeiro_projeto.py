def print_game(jogo):
    for index, item in enumerate(jogo, start=1):
        print(item, end='|' if index % 3 else '\n')

def verifica_vencedor(jogo):
    for i in jogo:
        if i[0] == i[1] == i[2]:
            print('Ganhou!!!')
            break
        elif i[3] == i[4] == i[5]:
            print('Ganhou!!!')
            break
        elif i[6] == i[7] == i[8]:
            print('Ganhou!!!')
            break


print('Jogo da Velha\n')
jogo = [' ',' ',' ',
        ' ',' ',' ',
        ' ',' ',''
        ]
print_game(jogo)

jog1 = input('\nJogador 1 deseja usar X ou O? \n')

if jog1[0] == 'X':
    jog2 = 'O'
else:
    jog2 = 'X'

# print(jog1)
# print(jog2)

i = 0
j = 0
while(i<9):
    i += 1
    index = int(input('\nJogador 1, qual posição vc deseja inserir o {}?'.format(jog1)))
    jogo[index] = jog1
    print_game(jogo)
    index = int(input('\nJogador 2, qual posição vc deseja inserir o {}?'.format(jog2)))
    jogo[index] = jog2
    print_game(jogo)
    


    