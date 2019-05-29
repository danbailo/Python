grafo = {}
grafo['meia'] = ['sapato']
grafo['relogio'] = []
grafo['roupa'] = ['calca', 'sapato']
grafo['camisa'] = ['cinto', 'gravata']
grafo['sapato'] = []
grafo['calca'] = ['cinto', 'sapato']
grafo['jaqueta'] = []
grafo['gravata'] = ['jaqueta']
grafo['cinto'] = ['jaqueta']

index = {}
index['meia'] = 0
index['relogio'] = 0
index['roupa'] = 0
index['camisa'] = 0
index['sapato'] = 0
index['calca'] = 0
index['jaqueta'] = 0
index['gravata'] = 0
index['cinto'] = 0

v = []

for i in grafo.values():
    for k in i:
       index[k] += 1

for i in index.keys():
   if i not in grafo.get(i):
       print(i)