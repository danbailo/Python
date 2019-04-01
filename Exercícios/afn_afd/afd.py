from string import ascii_letters as alphabet
class AFDState:
	def __init__(self,name):
		self.name=name
		self.t={}
		self.flag=""
	def __eq__(self,obj):
		if type(obj)==type(self):
			return obj.name==self.name
		elif type(obj)==str:
			return obj==self.name
		return False
	def __repr__(self):
		return self.__str__()
	def addTransition(self,symbol,child):
		if type(child)!=AFDState:raise RuntimeError("invalid child argument")
		self.t[symbol]=child
	def feed(self,symbol):
		try:return self.t[symbol]
		except KeyError:return None
	def __str__(self):
		return "AFDState(%s)"%self.name
class AFD:
	def __init__(self,q,sigma,delta,initial,finals):
		self.delta=delta
		self.q=[]
		for name in q:
			state=AFDState(name)
			if name==initial:
				state.flag+="i"
				self.initial=state
				self.reset()
			if name in finals:
				state.flag+="f"
			self.q.append(state)
		self.sigma=sigma
		m=len(delta)
		n=len(delta[0])
		if len(q)!=m or len(sigma)!=n:
			raise RuntimeError("invalid delta")
		for i in range(m):
			for j in range(n):
				statename=delta[i][j]
				if statename==None:continue
				child=None
				try:child=self.q[self.q.index(statename)]
				except ValueError:pass
				if child==None:continue
				self.q[i].addTransition(self.sigma[j],child)
			pass
	def reset(self):
		self.currstate=self.initial
	def isLanguage(self):
		if self.currstate==None:return False
		return "f" in self.currstate.flag
	def feed(self,word):
		for l in word:
			if l not in self.sigma:raise RuntimeError("word not in sigma")
			self.currstate=self.currstate.feed(l)
			if self.currstate==None:return False
		return self.isLanguage()

if __name__=="main":
	q=["q1","q2","q3"]
	sigma=alphabet+'0123456789'
	delta=[[],[],[]]
	for i in range(len(sigma)):
		if i<len(alphabet):delta[0].append("q2")
		else:delta[0].append("q3")

	delta[1]=["q2"]*len(sigma)
	delta[2]=["q3"]*len(sigma)
	#################################
	aut=AFD(q,sigma,delta,"q1",["q2"])


	print(aut.feed("abcd"))
	aut.reset()
	print(aut.feed("1ad"))
	aut.reset()
	print(aut.feed("3ad"))
	aut.reset()
	print(aut.feed("3aa"))
	aut.reset()
