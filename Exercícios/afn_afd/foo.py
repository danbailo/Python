class Epsilon:pass
class Convert_to_DFA:
	def __init__(self, states, sigma, delta, initial, final):

		self.states = states
		self.sigma = sigma
		self.delta = delta
		self.initial = initial
		self.final = final

	def get_states(self):
		new_states = [['{}'],self.states]
		for i in self.states:
			new_states.append([i])
			for j in self.states:
				if not i==j and (j,i) not in new_states:
					new_states.append((i,j))
		return new_states

	def get_sigma(self):
		return self.sigma

	def get_delta(self):
		new_delta = {}
		delta_keys = [i for i in self.delta.keys()]
		delta_values = [i for i in self.delta.values()]

		print('states: ',self.get_states())
		print('delta_keys: ',delta_keys)
		print('delta_values:')
		for i in delta_values:
			print(i)

		if delta_keys[0] in self.get_states():
			print('True')
		
		aux = 0
		for i in self.get_states():
			for j in delta_keys:
				if j in i and aux < len(self.delta):
					new_delta[j] = delta_values[aux]
					aux += 1
		
		
		
		print('new delta:',new_delta)

	def show_matrix(self):
		for i in self.delta.items():
			print(i)
		pass


states = ['q1','q2','q3']
sigma = ['a','b',Epsilon()]

#a,b,ε
delta = {}
delta['q1'] = [['{}'], ['q2'], ['q3']]
delta['q2'] = [['q2','q3'], ['q3'], ['{}']]
delta['q3'] = [['q1'], ['{}'], ['{}']]

initial = 'q1'
final = ['q1']

afd = Convert_to_DFA(states, sigma, delta, initial, final)

# print(afd.get_states())
# print(len(afd.get_states()))
afd.get_delta()
# afd.show_matrix()