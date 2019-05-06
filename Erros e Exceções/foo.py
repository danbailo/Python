try:
    a = 123/0
except ZeroDivisionError:
    print('impossivel dividir por 0')

while True:
    try:
        x = int(input('enter a integer: '))
        print('tks') #se o inteiro for inserio, ele continua a execucao e depois vai pro else
        #break #vai sair do laco, e nao entra no else
    except ValueError:
        print('only numbers integers')
    else:
        print('yeah, that is a integer!')
        break

print()

try:
    asdasd
    x = 1/0
except Exception as err:
    print('error: {}'.format(err))