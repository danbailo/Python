#Gerando todos os subconjuntos com backtracking
#subconjuntos = 2^n, onde n é o tamanho do conjunto original

def backtracking(S, array, K, N):
	sub = []
	if K == N:
		print('{',end=' ')
		for i in range(N):
			if array[i] == True:
				sub.append(S[i])
				print('{}' .format(sub), end=' ')
				# print('{}' .format(S[i]), end=' ')
		print('}')
	else:
		array[K] = True
		backtracking(S, array, K+1, N)
		array[K] = False
		backtracking(S, array, K+1, N)

S = ['q1','q2','q3','q4']
array = [False for i in range(len(S))]

x = backtracking(S, array, False, len(S))