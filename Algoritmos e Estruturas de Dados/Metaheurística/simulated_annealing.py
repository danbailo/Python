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
	def obj_fun(self, solution):
		return sum(solution)

	'''
		Simulated Annealing
		T -> temperatura inicial
		T_min -> temperatura mínima
		alpha -> decaimento da temperatura
		max_iter -> quantidade de iterações com uma mesma temperatura
	'''
	def run_anneal(self, T = 1.0, T_min = 0.00001, alpha = 0.9, max_iter = 100):

		while T > T_min:

			# iterações com uma mesma temperatura
			for i in range(max_iter):

				new_solution = self.neighbor() # gera uma nova solução
				new_cost = self.obj_fun(new_solution) # calcula o custo dessa nova solução
				delta = self.cost - new_cost # calcula a diferença dos custos
				ap = math.exp(-delta / T) # proababilidade de aceitação de uma solução de piora

				if ap > random.random(): # verifica se aceita ou não
					self.solution = new_solution[:] # copia a nova solução
					self.cost = new_cost # atribui o novo custo

			T = T * alpha

	def get_solution(self):
		return self.solution

one_max = OneMax(10)
print('Solução inicial: %s' % str(one_max.get_solution()))
one_max.run_anneal()
print('Solução final: %s' % str(one_max.get_solution()))