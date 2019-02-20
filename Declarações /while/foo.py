x = 1
y = 1

while (x < 10 and y < 20):
    print('x =',x)
    print('y =',y)
    print('O valor de x*y é:', x*y)
    x += 1
    y += 2
else:
    print('x =',x)
    print('y =',y)
    print('O valor de x*y é:', x*y)

x = 0

print('\n')

while x < 10:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x ==3:
        print('x==3')
        #break
    else:
        print('continuing...\n')
        continue
        #print('nao sera printado')

x = 0
while x <= 50:
    x += 1
    if x % 2 == 1:
        continue
    if x % 2 == 0:
        print(x,' é par')
    
x = 0
while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x ==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue