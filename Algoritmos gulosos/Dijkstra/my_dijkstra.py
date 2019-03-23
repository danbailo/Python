from collections import defaultdict
import heapq

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

#minheap
class MinHeap:
	def __init__(self):
		self.queue = []
		self.index = 0

	def insert(self, item, priority):
		heapq.heappush(self.queue,(priority, self.index, item))
		self.index += 1

	def remove(self):
		return heapq.heappop(self.queue)[-1] #desta tupla, retorna o "item" removido em si

	def length(self):
		return len(self.queue)

	def show(self):
		print(self.queue)

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
		self.vertexes = {} #armazenar os vertices

	def addEdge(self, src, dest, cost):
		self.graph[src].append((dest, cost))
		self.vertexes[src] = src
		self.vertexes[dest] = dest

	def dijkstra(self, src, dest):
		sol = []
		number_vertexes = len(self.vertexes)

		# estimativas de menor custo
		p = [ None for i in range(number_vertexes)]

		# estimativa para origem e 0
		if src != 0:
			p[src-1] = 0
		else:
			p[src] = 0

		print(p)

		#constroi a minheap
		minheap = MinHeap()
		minheap.insert(src, 0)

		#enquanto o tamanho da fila for maior q 0
		while minheap.length() > 0:
			# print(minheap.show())
			# print(minheap.show())

			#remove da fila de prioridade
			u = minheap.remove()
			print('u',u)
			sol.append(u)

			#adjacentes de u
			for edge in self.graph[u]:
				# print('edge: ', edge)
				#obtem o vertice adjacente e o custo (desempacotamento de tupla)
				v, cost = edge
				print(v,cost)

				# print(v)
				# print(cost)
				#relaxamento
				if p[v] is None or p[v] > p[u] + cost:
					print('oi')
					#atualiza a estimativa de custo
					p[v] = p[u] + cost

					#insere na fila de prioridades
					minheap.insert(v, p[v])


		#retorna o conjunto solucao e o custo do menor caminho
		return f7(sol),p[dest]

	def showConnections(self):
		for k,v in self.graph.items():
			print(k,v)


if __name__ == "__main__":
	g = Graph()

	g.addEdge(0, 1, 1)
	g.addEdge(0, 3, 3)
	g.addEdge(0, 4, 10)
	g.addEdge(1, 2, 5)
	g.addEdge(2, 4, 1)
	g.addEdge(3, 2, 2)
	g.addEdge(3, 4, 6)

	g.showConnections()

	s,c = g.dijkstra(0,4)

	print('Solucion is {} and cost is {}'.format(s,c))
	del g

	print()

	g = Graph()

	g.addEdge(5,4,5)
	g.addEdge(5,6,4)
	g.addEdge(5,3,10)
	g.addEdge(4,3,2)
	g.addEdge(4,1,2)
	g.addEdge(6,1,5)
	g.addEdge(6,4,1)
	g.addEdge(1,2,2)
	g.addEdge(3,2,3)

	g.showConnections()

	print(g.dijkstra(5,2))

	# g.addEdge('A','B',5)
	# g.addEdge('A','C',3)
	# g.addEdge('B','C',7)
	# g.addEdge('B','D',9)
	# g.addEdge('D','E',6)
	# g.addEdge('D','F',9)
	# g.addEdge('E','F',9)
	# g.showConnections()
	# print(g.dijkstra('A','F'))


