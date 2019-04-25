def busca_forc(A,l,r,x):
    if r>=l:
        meio = int((l+r)/2)
        if A[meio] == x: return 1
        r1 = busca_forc(A, l, meio-1, x)
        r2 = busca_forc(A, meio+1, r, x)
        if r1 == 1 or r2 == 1: return 1
        else: return -1

def busca_bin(A,l,r,x):
    if r>=l:
        indice = int((l+(r-l))/2)
        if(A[indice]==x): return 1
        if(A[indice]>x): return busca_bin(A, l, indice-1, x)
        return busca_bin(A, indice-1, r, x)
    return -1
        

array = [12,32,5,3,2,123,6,23]
array_ord = sorted(array)

print(busca_forc(array,0,len(array)-1,12))
print(busca_bin(array_ord,0,len(array)-1,6))
