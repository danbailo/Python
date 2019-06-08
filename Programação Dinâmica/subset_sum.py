def isSubsetSum(conjunto,n, soma) : 
    if (soma == 0) : return True
    if (n == 0 and soma != 0) : return False
    return max(isSubsetSum(conjunto, n-1, soma),isSubsetSum(conjunto, n-1, soma-conjunto[n-1]))

if __name__ == "__main__":
    conjunto = [1, 3, 7, 9, 11] 
    n = len(conjunto)
    while True:
        soma = int(input('input a sum: '))
        print(isSubsetSum(conjunto, n, soma))