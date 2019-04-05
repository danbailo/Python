class Graph:

	def __init__(self, vertices): 
		self.vertices = vertices
		self.graph = [[] for i in range(vertices)]

	def add_edge(self, u, v): #graph directed
		self.graph[u].append(v)

	def show(self):
		for i in range(self.vertices):
			print('%d: ' % i, end=' ')
			for j in self.graph[i]:
				print('%d -> ' %j, end=' ')
			print('')

graph = Graph(5)

graph.add_edge(0, 1)
graph.add_edge(3, 0)
graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(4, 2)

graph.show()