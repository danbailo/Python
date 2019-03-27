from collections import defaultdict

class AFN:
	def __init__(self, states, sigma, delta, initial, final):
		self.states = states
		self.sigma = sigma
		self.delta = delta
		self.initial = initial
		self.final = final

	def get_states(self):
		s = ['{}']
		for j in self.states:
			s.append((j))
			for k in self.states:
				if not j==k and (k,j) not in s:
					s.append((j,k))	
		s.append(self.states)
		return s

	def get_sigma(self):
		return self.sigma

	def get_delta(self):
		print('delta: ',self.delta)
		print('\nstates: ',self.get_states())

states = ('q1','q2','q3')
sigma = ('a','b','ε')

#especificidade do automato
# delta = [
# 	['{}','q2','q3'],
# 	[('q2','q3'),'q3','{}'],
# 	['q1','{}','{}']
# ]

# delta = defaultdict(list)
# delta[('q1','a')].append('{}')

delta = {}
delta[('q1','a')] = ['{}']
delta[('q1','b')] = ['q2']
delta[('q1','ε')] = ['q3']
delta[('q2','a')] = ['q2','q3']
delta[('q2','b')] = ['q3']
delta[('q2','ε')] = ['{}']
delta[('q3','a')] = ['q1']
delta[('q3','b')] = ['{}']
delta[('q3','ε')] = ['{}']

# print(delta)

initial = 'q1'
final = ('q1')

afd = AFN(states, sigma, delta, initial, final)

# print(afd.convert_states()[1][0])
# print(afd.get_states())
# afd.get_states()
afd.get_delta()