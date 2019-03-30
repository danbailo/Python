class Convert_to_DFA:
	def __init__(self, states, sigma, delta, initial, final):
		self.states = states
		self.sigma = sigma
		self.delta = delta
		self.initial = initial
		self.final = final

	def get_states(self):
		new_states = ['{}',self.states]
		for j in self.states:
			new_states.append((j))
			for k in self.states:
				if not j==k and (k,j) not in new_states:
					new_states.append((j,k))
		return new_states

	def get_sigma(self):
		return self.sigma

	def get_delta(self):
		for i in self.delta.values():
			print(i[0])
		pass


states = ('q1','q2','q3')
sigma = ('a','b') #I've remove the 'ε'

#a,b,ε
delta = {}
delta['q1'] = [['{}'], ['q2'], ['q3']]
delta['q2'] = [['q2','q3'], ['q3'], ['{}']]
delta['q3'] = [['q1'], ['{}'], ['{}']]

initial = 'q1'
final = ('q1')

afd = Convert_to_DFA(states, sigma, delta, initial, final)

afd.get_delta()
