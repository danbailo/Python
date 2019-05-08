def mdc(a,b):
    if b==0: return a
    return mdc(b,a%b)

def mmc(a,b):
    return a*b/mdc(a,b)

def less_number(array, left, right):
    middle = int((left+right)/2)
    if left == right:
        return array[left]
    x = less_number(array, left, middle)
    y = less_number(array, middle+1, right)
    if x > y: return y
    else: return x

def busca_menor(A,l,r):
    meio = int((l+r)/2)
    if l == r: return A[l]
    x = busca_menor(A, l, meio)
    y = busca_menor(A, meio+1, r)
    if x > y: return y
    else: return x              


print(mdc(20,12))

print(mmc(20,25))

array = [23,12,5,66,7,23,1,29,6]

print(busca_menor(array,0,len(array)-1))
print(less_number(array,0,len(array)-1))