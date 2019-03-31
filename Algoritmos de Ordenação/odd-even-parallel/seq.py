import time

def oddevenSort(x):
    sorted = False
    while not sorted:
        sorted = True

        #ordena indices par/impar
        for i in range(0, len(x)-1, 2):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                sorted = False

        #ordena indices impar/par
        for i in range(1, len(x)-1, 2):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                sorted = False
    print(x)
    return x


tic = time.time()
oddevenSort([4,3,2,1,3,6,9,1,2,3,54,76,98,12,333,331,33,1,7,9])
toc = time.time()

print("tempo gasto para processar = " + str(toc-tic)+"s")