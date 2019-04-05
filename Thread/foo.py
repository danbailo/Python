from threading import Thread
import time

def func(i):
    print('Iniciando a thread %d' %i)
    time.sleep(5)
    print('Thread %d finalizada' %i)

for i in range(10):
    t = Thread(target=func, args=(i,))
    t.start()

	asdsa;