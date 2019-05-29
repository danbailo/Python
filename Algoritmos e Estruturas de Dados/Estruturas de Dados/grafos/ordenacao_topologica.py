import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def plot_graph(theGraph):
    n=len(theGraph)    
    nxGraph=nx.DiGraph()
    for i in range(n):
        for j in theGraph[i]:
            nxGraph.add_edge(i,j)
    labels={}
    for i in range(n):
        labels[i]=str(i)
    pos=nx.spring_layout(nxGraph)
    nodeList=range(n)
    nx.draw_networkx_nodes(nxGraph,pos,node_color='r',node_size=500)
    nx.draw_networkx_edges(nxGraph,pos,width=1.0,alpha=0.5,arrows=True)
    nx.draw_networkx_labels(nxGraph,pos,labels,font_size=16)
    plt.axis('off')
    plt.show()
    # plt.savefig("theGraph.eps")    

def top_sort(theGraph):
    n=len(theGraph)
    topSort=-np.ones([n])    
    numberIncomeEdges=np.zeros([n])
    setOfNodesWithNoActiveEdges=set()
    # Loop O(m+n)
    for i in range(n):
        for j in theGraph[i]:
            numberIncomeEdges[j]=numberIncomeEdges[j]+1
    #O(n)
    for i in range(n):
        if(numberIncomeEdges[i]==0):
            setOfNodesWithNoActiveEdges.add(i)
    i=0
    #O(m+n)
    while((i<n) and (len(setOfNodesWithNoActiveEdges)!=0)):
        i=i+1
        node=setOfNodesWithNoActiveEdges.pop()
        topSort[i-1]=node
        for j in theGraph[node]:
            numberIncomeEdges[j]=numberIncomeEdges[j]-1
            if(numberIncomeEdges[j]==0):
                setOfNodesWithNoActiveEdges.add(j)

    if(i!=n):
        print("The graph is not a dag")
    else:
        print(topSort)






if __name__ == '__main__':
    """
    n=6 #number of nodes

    theGraph=[set() for i in range(n)]
    theGraph[0].add(1)
    theGraph[0].add(2)
    theGraph[1].add(0)
    theGraph[1].add(3)
    theGraph[2].add(0)
    theGraph[2].add(4)
    theGraph[3].add(1)
    theGraph[3].add(5)
    theGraph[4].add(2)
    theGraph[4].add(5)
    theGraph[5].add(3)
    theGraph[5].add(4)
    """
    n=7 #number of nodes

    theGraph=[set() for i in range(n)]

    theGraph[0].add(3)
    theGraph[0].add(4)
    theGraph[0].add(6)    
    theGraph[1].add(2)
    theGraph[1].add(4)
    theGraph[1].add(5)    
    theGraph[2].add(3)
    theGraph[2].add(4)
    theGraph[3].add(4)
    theGraph[4].add(5)
    theGraph[4].add(6)
    theGraph[5].add(6)


    plot_graph(theGraph)

    top_sort(theGraph)