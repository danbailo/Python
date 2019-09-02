from threading import Thread
from time import sleep

def caminho1(i,j):
    sleep(.1)
    print(i,j)
def caminho2(i,j):
    print(i,j)
t1=Thread(target=caminho1, args=(1,2))
t2=Thread(target=caminho2,args=(3,4))

t1.start()
t2.start()