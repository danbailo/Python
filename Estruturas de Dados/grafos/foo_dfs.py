from string import ascii_uppercase as alphabet
#dfs - Depth-first_search ( busca em profundidade )
#http://www.algolist.net/Algorithms/Graph/Undirected/Depth-first_search
#https://techdifferences.com/difference-between-bfs-and-dfs.html

class Graph(object): 
    def __init__(self, vertices): #adjacency matrix
        self.vertices = vertices
        self.graph = [[0]*vertices for i in range(vertices)]
        #print(self.graph) - debugger
        #initializes all index of matrix with 0.
        #[] for i in range(vertices) error
        #[0] for i in range(vertices) - only lines get him
        self.visited = [False] * vertices #none node was visited


    def add_edge(self, u, v): #not directed graph 
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def show(self): # adjacency matrix, i.e. look at line and column
        # for i in range(self.vertices):
        #     print(alphabet[i], end=' ')
        # print('')
        x = 1
        for i in self.graph:
            print(x, end=' - ')
            x += 1
            for j in i:
                print(j, end=' ')
            print('') #break a line

    def linked(self, u, v):
        if self.graph[u][v] == 1:
            return True
        return False

    def dfs(self,u):
        self.visited[u] = True
        print('%d visited' %(u+1))
        for i in range(self.vertices):
            if self.linked(u,i) == True and self.visited[i] == False:
                self.dfs(i)



#[0] * 5 = [0, 0, 0, 0, 0]

#a,b,c,d,e
#0,1,2,3,4

# A - C
# B - C
# C - D
# C - E
# D - E

# graph = Graph(5)

# graph.add_edge(2,0)
# graph.add_edge(2,1)
# graph.add_edge(2,3)
# graph.add_edge(2,4)
# graph.add_edge(3,4)

# graph.show()

# print(graph.linked(1,3))
# print(graph.linked(0,2))

g = Graph(5)

g.add_edge(0,3)
g.add_edge(3,1)
g.add_edge(3,4)
g.add_edge(1,4)
g.add_edge(4,2)

g.show()
print('')
g.dfs(0)