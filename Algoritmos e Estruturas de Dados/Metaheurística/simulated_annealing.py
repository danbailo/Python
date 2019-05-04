# Onemax Problem with Simulated Annealing

import random, math

class OneMax:

	def __init__(self, size):
		self.size = size
		self.solution = [random.randint(0, 1) for i in range(size)]
		self.cost = self.obj_fun(self.solution)

	# gera um vizinho
	def neighbor(self):
		new_neighbor = self.solution[:]##########copia a lista, no caso, se eu tivesse feito somente para receber, 											
		pos = random.randint(0, self.size - 1)  #as duas variaveis iriam apontar para o mesmo endereço, logo, modificando o conteudo de um, modificaria as duas
		new_neighbor[pos] = 1 if new_neighbor[pos] == 0 else 0
		return new_neighbor

	# função objetivo
	def obj_fun(self, solution): #se a soma estiver mais perto do tamanho, melhor
		return sum(solution)

	'''
		Simulated Annealing
		T -> temperatura inicial
		T_min -> temperatura mínima
		alpha -> decaimento da temperatura
		max_iter -> quantidade de iterações com uma mesma temperatura
	'''
	def run_anneal(self, T = 1, T_min = 0.00001, alpha = 0.9, max_iter = 100):

		while T > T_min:

			# iterações com uma mesma temperatura
			for _ in range(max_iter):
				print()
				print('solution:',self.solution)
				new_solution = self.neighbor() # gera uma nova solução
				print('new_solution:',new_solution)
				new_cost = self.obj_fun(new_solution) # calcula o custo dessa nova solução
				print('new_cost:',new_cost)
				delta = self.cost - new_cost # calcula a diferença dos custos
				print('delta:',delta)
				ap = math.exp(-delta / T) # proababilidade de aceitação de uma solução de piora
				print('approved:',ap)

				if ap > random.random(): # verifica se aceita ou não
					print('approved is larger than random')
					self.solution = new_solution[:] # copia a nova solução
					self.cost = new_cost # atribui o novo custo

			print("temperature:",T)
			T = T * alpha

	def get_solution(self):
		return self.solution

# 1e-05 == 0.00001
# 1.0290430145553226e-05 == 0.000010290430145553226

one_max = OneMax(10)

print('Initial solution: %s' % str(one_max.get_solution()))
one_max.run_anneal()
print()
print('Final solution: %s' % str(one_max.get_solution()))
