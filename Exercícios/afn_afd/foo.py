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
		pass

states = ('q1','q2','q3')
sigma = ('a','b','ε')
delta = []
initial = 'q1'
final = ('q1')

def set_delta(states, sigma):
	global delta
	for i in states:
		for j in sigma:
			delta.append((i,j))
	return delta

set_delta(states,sigma)

print(delta)

afd = AFN(states, sigma, delta, initial, final)

# print(afd.convert_states()[1][0])
print(afd.get_states())
# afd.get_states()
# afd.get_delta()