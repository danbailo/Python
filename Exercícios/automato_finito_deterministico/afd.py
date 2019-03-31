from string import ascii_letters as alphabet
class State:
	def __init__(self,name):
		self.name=name
		self.t={}
		self.flag=""
	def addTransition(self,symbol,child):
		self.t[symbol]=child
	def feed(self,symbol):
		try:return self.t[symbol]
		except KeyError:return None
class Automaton:
	def __init__(self,q,sigma,gamma,initial,finals):
		self.q=[]
		for name in q:
			state=State(name)
			if name==initial:
				state.flag="i"
				self.initial=state
				self.reset()
			elif name in finals:
				state.flag="f"
			self.q.append(state)
		self.sigma=sigma
		m=len(gamma)
		n=len(gamma[0])
		if len(q)!=m or len(sigma)!=n:
			raise RuntimeError("invalid gamma")
		for i in range(m):
			for j in range(n):
				statename=gamma[i][j]
				if statename==None:continue
				child=None
				for state in self.q:
					if state.name==statename:
						child=state
						break
					pass
				if child==None:continue
				self.q[i].addTransition(self.sigma[j],child)
			pass
	def reset(self):
		self.currstate=self.initial
	def feed(self,word):
		for l in word:
			if l not in self.sigma:raise RuntimeError("word not in sigma")
			self.currstate=self.currstate.feed(l)
			if self.currstate==None:return False
		return self.currstate.flag=="f"
q=["q1","q2","q3"]
sigma=alphabet+'0123456789'
gamma=[[],[],[]]
for i in range(len(sigma)):
	if i<len(alphabet):gamma[0].append("q2")
	else:gamma[0].append("q3") #seria aqui que ele exclui as palavras que começam com numeros?

gamma[1]=["q2"]*len(sigma)
gamma[2]=["q3"]*len(sigma)
#################################
aut=Automaton(q,sigma,gamma,"q1",["q2"])

# while True:
# 	print(aut.feed(input()))
# 	aut.reset()
