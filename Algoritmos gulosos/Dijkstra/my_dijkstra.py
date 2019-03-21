from collections import defaultdict

class Graph:
    def __init__(self, graph_dict = None):
        if graph_dict == None: 
            graph_dict = defaultdict(list)
        self.graph_dict = graph_dict

    def add_edge(self, u, v):
        self.graph_dict[u].append(v)

    def show_connections(self):
        for k,v in self.graph_dict.items():
            print(k,v)

g = Graph()

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)

g.show_connections()

# d = {'key1':4, 'key2':6, 'key3': 8}

# print(d)
# print(d.items())

# for k,v in d.items():
#     print(k,v)