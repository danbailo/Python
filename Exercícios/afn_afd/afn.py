from afd import AFD,AFDState
import threading
import copy
import traceback
class Epsilon:
	def __eq__(self,obj):
		return type(obj)==Epsilon
	def __hash__(self):
		return hash("Epsilon")
	def __str__(self):
		return "(Epsilon)"
	def __repr__(self):
		return self.__str__()
class AFNState(AFDState):
	def __init__(self,afdstate):
		if type(afdstate)!=AFDState:raise ValueError()
		self.name=afdstate.name
		self.t=afdstate.t
		self.flag=afdstate.flag
	def __str__(self):
		return "AFNState(%s)"%self.name
	def addTransition(self,symbol,childlist):
		if type(childlist)!=list:raise RuntimeError("invalid childlist argument")
		for c in childlist:
			if type(c)!=AFNState:raise RuntimeError("invalid childlist argument")
		self.t[symbol]=childlist

class AFN(AFD):
	def __init__(self,q,sigma,delta,initial,finals):
		self.threads=[]
		if Epsilon()!= sigma[0]:raise RuntimeError("Epsilon must be the first in the alphabet")
		super().__init__(q,sigma,delta,initial,finals)
		for i in range(len(self.q)):
			self.q[i]=AFNState(self.q[i])
			if "i" in self.q[i].flag:
				self.initial=self.q[i]
		m=len(delta)
		n=len(delta[0])
		for i in range(m):
			for j in range(n):
				statename=delta[i][j]
				if statename==None:continue
				if type(statename)!=list:raise RuntimeError("invalid delta")
				child=[]
				for childname in statename:
					try:child.append(self.q[self.q.index(childname)])
					except ValueError:raise RuntimeError("Invalid delta")
				if child==[]:continue
				self.q[i].addTransition(self.sigma[j],child)
			pass
		self.reset()
	def reset(self):
		if type(self.initial)==AFDState:return
		self.currstate=self.initial
		for t in self.threads:t[1].join()
		self.threads=[]
	def isLanguage(self):
		ans=super().isLanguage()
		for t in self.threads:
			t[1].join()
			ans|=t[0].isLanguage()
		return ans
	def feed(self,word):
		th=hex(threading.get_ident())
		# print("[starting] %s: word:%s currstate:%s"%(th,word,self.currstate))
		if self.currstate==None:return False
		for i in range((len(word)*2)+1):
			wi=int((i-1)/2)
			l=Epsilon() if (i%2)==0 else word[wi]
			if l not in self.sigma:raise RuntimeError("word not in sigma")
			nextState=copy.copy(self.currstate.feed(l))
			if nextState in [None,[]]:
				if l == Epsilon():continue
				self.currstate=None
				return False
			self.currstate=nextState.pop()
			for remainingState in nextState:
				obj=copy.deepcopy(self)
				obj.currstate=remainingState
				t=threading.Thread(target=AFN.feed, args=(obj,word[wi::],))
				t.start()
				self.threads.append([obj,t])
			pass
		return self.isLanguage()


if __name__=="__main__":
	q=["q1","q2","q3","q4","q5","q6"]
	sigma=[Epsilon(),"0"]
	delta=[[] for _ in q]

	delta[0]=[["q2","q3"],None]
	delta[1]=[None,      ["q4"]]
	delta[2]=[None,      ["q5"]]
	delta[3]=[None,      ["q2"]]
	delta[4]=[None,      ["q6"]]
	delta[5]=[None,      ["q3"]]

	initial="q1"
	finals=["q2","q3"]
	
	aut=AFN(q,sigma,delta,initial,finals)
	msg=""
	print(msg,aut.feed(msg))
	aut.reset()
	msg="0"
	print(msg,aut.feed(msg))
	aut.reset()
	msg="00"
	print(msg,aut.feed(msg))
	aut.reset()
	msg="000"
	print(msg,aut.feed(msg))
	aut.reset()
	msg="0000"
	print(msg,aut.feed(msg))
	aut.reset()
	msg="00000"
	print(msg,aut.feed(msg))
	aut.reset()
	msg="000000"
	print(msg,aut.feed(msg))
	aut.reset()
