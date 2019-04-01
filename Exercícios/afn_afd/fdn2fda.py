from afd import AFD,AFDState
from afn import AFN,AFNState,Epsilon
from itertools import chain,combinations
def powerset(s):
    ans=list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    return [list(elem) for elem in ans]
def depthSearchEpsilon(fdn,state):
	ans=[]
	stack=[state]
	while(stack!=[]):
		aux=stack.pop()
		ans.append(aux.name)
		feed=aux.feed(Epsilon())
		if feed==None:continue
		stack+=feed
	ans.sort()
	return ans
def fdn2fda( fdn ):
	states=[elem.name for elem in fdn.q]
	new_states_name=powerset(states)
	new_initial_name=depthSearchEpsilon(fdn,fdn.initial)
	new_initial_name=str(new_initial_name)

	new_final_names=[]
	final=[]
	for elem in fdn.q:
		if "f" in elem.flag:
			final.append(elem.name)
	for f in final:
		for n in new_states_name:
			if (f in n) and (n not in new_final_names):
				new_final_names.append(n)
	
	new_delta=[list() for _ in range(len(new_states_name))]
	s=len(fdn.sigma)-1

	new_delta[0]=[[]]*s
	#estados n==1
	for i,qs in enumerate(fdn.delta):
		for j in range(s):
			temp=fdn.delta[i][j+1]
			if temp!=None:
				ds=set()
				for t in temp:
					ds=ds.union(depthSearchEpsilon(fdn,fdn.q[fdn.q.index(t)]))
				temp=list(set(temp).union(ds))
				temp.sort()

			new_delta[i+1].append(temp)


	#estados n>1
	for i,sn in enumerate(new_states_name[1::]):
		if len(sn)==1:continue
		for j in range(s):
			u=set()
			for k in sn:
				temp=new_delta[new_states_name.index([k])][j]
				if temp==None:continue
				u=u.union(temp)
			u=list(u)
			u.sort()
			new_delta[i+1].append(u)
		pass
	#limpar, converter tudo para str
	for i in range(len(new_states_name)):
		new_states_name[i]=str(new_states_name[i])
	for i in range(len(new_delta)):
		for j in range(len(new_delta[i])):
			elem=new_delta[i][j]
			if elem==None:
				new_delta[i][j]="[]"
			else:
				new_delta[i][j]=str(elem)

	# print("q:",new_states_name)
	# print("sigma:",fdn.sigma[1::])

	# print("delta:")
	# for r in new_delta:
	# 	print(r)
	# print("initial:\"%s\""%new_initial_name)
	# print("finals:",new_final_names)
	return AFD(new_states_name,fdn.sigma[1::],new_delta,new_initial_name,new_final_names)	
	
states = ['q1','q2','q3']
sigma = [Epsilon(),'a','b']
delta = [[],[],[]]
delta[0] = [['q3'],None,        ['q2']]
delta[1] = [None,['q2','q3'], ['q3']]
delta[2] = [None ,['q1']       , None]

initial = 'q1'
final = ['q1']

fdn=AFN(states, sigma, delta, initial, final)
fda=fdn2fda(fdn)

while(True):
	u=input()
	print("AFN:%s AFD:%s"%(fdn.feed(u),fda.feed(u)))
	fdn.reset()
	fda.reset()