from functools import reduce

#A função reduce(função, sequência) aplica continuamente a função à sequência. 
# Em seguida, ele retorna um único valor.

#Se seq = [s1, s2, s3, ..., sn], a redução de chamada (função, sequência) funciona assim:

#No início, os dois primeiros elementos de seq serão aplicados à função, isto é, func(s1, s2)
# A lista em que a reduce() funciona parece assim: [função (s1, s2), s3, ..., sn]
# No próximo passo, a função será aplicada no resultado anterior e no terceiro elemento da lista, ou seja, função(função (s1, s2), s3)
# A lista parece agora: [função (função (s1, s2), s3), ..., sn]
# Continua assim até apenas um elemento é deixado e retorna esse elemento como resultado de reduzir ()

lst =[47,11,42,13]
print(reduce(lambda x,y: x+y,lst))

# from IPython.display import Image
# Image('reduce_diagram.png')

#Find the maximum of a sequence (This already exists as max())
max_find = lambda a,b: a if (a > b) else b
#return a if a>b else return b

print(reduce(max_find,lst))