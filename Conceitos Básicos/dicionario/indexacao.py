d = {'total':'1', 'contacts':{
	'210':{
		'isPublished':True,
		'dataAdded':'2019...',
		'id':210
	}}}

print(d.keys())
print(d['contacts'].keys())

x = list(d['contacts'].keys())

print('x:',type(x[0]))

print(d['contacts']['210'].values())


for i in d['contacts']['210'].values():
	if i == 210:
		print('is my id!')

for i in d['contacts']['210'].keys():
	print(i)

# print(d.keys())