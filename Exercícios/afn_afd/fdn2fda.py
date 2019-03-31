# from afd import AFD,AFDState
# from afn import AFN,AFNState
class Epsilon:pass
def fdn2fda( states, sigma, delta, initial, final):
	new_states_name = [[],states]
	for i in states:
		new_states_name.append([i])
		for j in states:
			if i==j:continue
			temp=[i,j]
			temp.sort()
			if temp not in new_states_name:
				new_states_name.append(temp)
			pass
		pass
	new_states_name.sort(key=len)
	new_initial_name=[]
	aux=initial
	while(True):
		if aux==None:break
		new_initial_name.append(aux.name)
		aux=aux.feed(Epsilon())
	new_initial_name.sort()
	new_initial_name=str(new_initial_name)

	new_final_names=[]
	for f in final:
		for n in new_states_name:
			if (f in n) and (n not in new_states_name):
				new_final_names.append(n)
	new_delta=[[] for range(len(new_states_name))]
	#vazio
	new_delta[0]=[str([])]*len(sigma)
	#primitivo
	for i,sn in enumerate(new_states_name[1::]):
		if len(sn)!=1:continue
		for j in range(len(sigma)):
			new_delta[i+1].append(str(delta[i+1][j]))
		pass
	#deltadelta
	for i,sn in enumerate(new_states_name[1::]):
		if len(sn)==1:continue
		for j in range(len(sigma)):
			u=set()
			for k in delta[i+1][j].translate(str.maketrans(dict.fromkeys("[]"))).split(","):
				u.union(new_delta[new_states_name.index(k)][j])
			new_delta[i+1].append(u)
		pass



	
	
	
states = ['q1','q2','q3']
sigma = ['a','b',Epsilon()]

#a,b,ε
delta = [[],[],[]]
delta[0] = [['{}'], ['q2'], ['q3']]
delta[1] = [['q2','q3'], ['q3'], ['{}']]
delta[2] = [['q1'], ['{}'], ['{}']]

initial = 'q1'
final = ['q1']
fdn2fda(states, sigma, delta, initial, final)