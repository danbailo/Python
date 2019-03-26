from collections import defaultdict

class Graph:
	def __init__(self):
		self.list_neighbor = defaultdict(list)

	def add_edge(self, initial, final):
		self.list_neighbor[initial].append(final)

class AFN:
	def __init__(self, states, sigma, delta, initial, final):
		self.states = states
		self.sigma = sigma
		self.delta = delta
		self.initial = initial
		self.final = final

	def get_states(self):
		s = ['{}', self.states]
		for j in self.states:
			s.append((j))
			for k in self.states:
				if not j==k and (k,j) not in s:
					s.append((j,k))
		return s

	def get_sigma(self):
		return self.sigma

	def get_delta(self):
		print(self.get_states())

# delta = {'q1':'q2,q3','q2':'q2,q3','q3':'q1'}

delta = Graph()

delta.add_edge('q1','q2')

afd = AFN(('q1','q2','q3'), ('a','b'), 'delta', 'q1', ('q1'))

# print(afd.convert_states())
# print(afd.convert_states()[1][0])
# afd.get_states()
afd.get_delta()