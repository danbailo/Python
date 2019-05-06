def busca_maior(A,l,r):
    meio = int((l+r)/2)
    if l == r: return A[l]
    x = busca_maior(A, l, meio)
    y = busca_maior(A, meio+1, r)
    if x > y: return x
    else: return y      
        
array = [23, 12, 15, 66, 88, 1111, 2, 9, 45]
print(busca_maior(array, 0, len(array)-1))