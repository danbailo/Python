from string import ascii_uppercase as alphabet
#bfs - Breadth-first search ( busca em largura )
#https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
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

    def bfs(self, v):
        viseted = [False] * self.vertices #vertices not visited
        viseted[v] = True
        queue = [v]
        
        print('%d visited' %v)

        while len(queue) > 0:
            v = queue[0]   

            for u in range(self.vertices): #0,1; 0,2; 0,3; 0,4
                if self.graph[v][u] == 1:
                    if viseted[u] == False:
                        viseted[u] = True
                        queue.append(u)
                        # print(queue)
                        print('%d visited' %u)
            print(queue)
            queue.pop(0)


g = Graph(5)

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(2, 3)

g.bfs(0)

viseted = [False] * 5
viseted[0] = True
queue = [0]

# print(viseted)
# print(queue)
# print(len(queue))
# queue.pop()
# print(len(queue))
