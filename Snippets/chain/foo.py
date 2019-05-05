from itertools import chain

#2D list / matrix 2x2
l1 = [
    [1,2,3],
    [4,5,6]
    ]

print(l1)

#convert to 1D list / vetor, array
l2 = list(chain.from_iterable(l1))

print(l2)