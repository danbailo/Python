def fib(n):
    x,y=1,1
    for i in range(n):
        x,y=x+y,x
        yield x
list(range(10))