class Graph:
	def __init__(self, vertex):
		self.vertex = vertex
		self.list = [[] for i in range(self.vertex)]

	def add_edge(self, u, v):
		self.list[u].append(v)

	def dfs(self, vertex):
		stack = []
		visited = [False for i in range(self.vertex)] #[False, False, False]
		stack_record = [False for i in range(self.vertex)]


		while True:
			found_neighbor = False
			
			if not visited[vertex]:
				stack.append(vertex)
				visited[vertex] = stack_record[vertex] = True

			# aux_neighbor = None

			for neighbor in self.list[vertex]:
				# aux_neighbor = neighbor

				if stack_record[neighbor]:
					return True

				elif not visited[neighbor]:
					found_neighbor = True
					break
			
			if not found_neighbor:
				stack_record[stack[-1]] = False
				stack.pop()
				if len(stack) == 0:
					break
				vertex = stack[-1]
			
			else:
				vertex = neighbor
	 	
		return False
	
	def has_cycle(self):
		for i in range(self.vertex):
			if self.dfs(i):
				return True
		return False

	def show(self):
		index = 0
		for i in self.list:
			print(index,'->',i)
			index += 1

g = Graph(4)

g.add_edge(0, 0)
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.add_edge(3,3)

g.show()

print(g.has_cycle())