x = 3
y = 7

def increment():
    global x,y #falando pro python q eu quero utilizar as variaveis globais x e y
    x += 5
    y += 3

print('x is {} and y is {}'.format(x,y))

#increment x,y value
increment()

print('x is {} and y is {}'.format(x,y))
