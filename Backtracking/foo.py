#Gerando todos os subconjuntos com backtracking
#subconjuntos = 2^n, onde n é o tamanho do conjunto original

def backtracking(S, array, K, N):
	if K == N:
		print('{',end=' ')
		for i in range(N):
			if array[i] == True:
				print('%d ' % S[i], end=' ')
		print('}')
	else:
		array[K] = True
		backtracking(S, array, K+1, N)
		array[K] = False
		backtracking(S, array, K+1, N)

S = [1,2]
array = [False for i in range(len(S))]

backtracking(S, array, False, len(S))