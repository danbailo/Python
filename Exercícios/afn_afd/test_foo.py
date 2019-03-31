S = ['q1','q2','q3']

states = []
for i in S:
	states.append([i])
	for j in S:
		print('i: ',i)
		print('j: ',j)
		print((i,j))
		if not i==j and (j,i) not in states:
			states.append([i,j])
			print('append: ',[i,j])

# print(states)
print(len(states))