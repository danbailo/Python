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
		pass

afd = AFN(('q1','q2','q3'), 'ab', 'delta', 'q1', ['q1'])

# print(afd.convert_states())
# print(afd.convert_states()[1][0])
# afd.convert_states2()
print(afd.get_states())