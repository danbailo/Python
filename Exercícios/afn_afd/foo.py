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
		for i in self.get_states():
			print('states: ',i)
		
		for i in self.delta.keys():
			print('keys: ',i)

		for i in self.delta.items():
			print('items: ',i)

	def get_delta2(self):
		new_delta = {}
		n = 0
		# print((self.states[0],self.states[1]))
		# print((self.states[0],self.states[2]))
		# print((self.states[1],self.states[0]))
		# print((self.states[1],self.states[2]))
		# print((self.states[0],self.states[1]))
		# print(self.states[0]+self.states[1])
		print('items')
		for i in self.delta.items():
			print(i)
		print()
		
		for i in self.get_states():
			print('state: ',i)
			for j in self.get_sigma():
				# try:
				# 	if i == (self.states[n],self.states[n+1]): #TESTAR COM MAIS CONDICIONAIS, PASSANDO ELIFS COM INDEXACAO DE OUTROS VALORES
				# 		print('primeiro if ',(self.states[n],self.states[n+1]))
				# 	elif i == (self.states[n],self.states[n+2]):
				# 		print('segundo if ',(self.states[n],self.states[n+2]))
				# 	n += 1
				# except IndexError:
				# 	n -= 1
					# print('indexerror')
				if (i,j) in self.delta.keys():
					new_delta[(i,j)] = self.delta[(i,j)]
					# print('i,j: ',(i,j))
					print('delta i,j: ',self.delta[i,j])
				elif i == self.states:
					# print('i: ',i)
					# print('j: ',j)
					new_delta[(i,j)] = ['ok, I want repair state']
							
		return new_delta


states = ('q1','q2','q3')
sigma = ('a','b') #i remove the 'ε'

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

# print(delta)

initial = 'q1'
final = ('q1')

afd = Convert_to_DFA(states, sigma, delta, initial, final)

# print(afd.convert_states()[1][0])
# print(afd.get_states())
# afd.get_states()

# afd.get_delta()
# afd.get_delta2()

for i,k in afd.get_delta2().items():
	print(i,k)