from collections import deque

d = deque()
 
d.append(5) #adiciona na direita
d.appendleft(1) #adiciona na esquerda
d.append(7)
d.append(9)
d.appendleft(23)

for i in d:
    print(i, end=' ')
    
print('\n')