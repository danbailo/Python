from graphviz import Digraph
from afd import *

aut=Automaton(q,sigma,gamma,"q1",["q2"])

f = Digraph('automato_finito_deterministico', filename='afd.gv')
f.attr(rankdir='LR', size='7')

node = 0
while node<len(aut.q):
    if aut.q[node].flag=="f":
        f.attr('node', shape='doublecircle')
    else:
        f.attr('node', shape='circle')
    f.node(aut.q[node].name)
    node += 1

edges = 0
while edges<len(aut.q):
    if aut.q[edges].flag=="i":
        f.attr('node', shape='none')
        f.edge('', aut.q[edges].name,)
    elif aut.q[edges].flag=="f":
        f.edge(aut.q[0].name, aut.q[edges].name, label = 'a, ..., z, A, ..., Z, 0, ..., 9')
        f.edge(aut.q[edges].name, aut.q[edges].name, label = 'a, ..., z, A, ..., Z, 0, ..., 9')
    else:
        f.edge(aut.q[0].name, aut.q[edges].name, label = '0, 1, 2, 3, 4, 5, 6, 7, 8, 9')
        # f.edge_attr.update(fontsize ='7')
        f.edge_attr = {'fontsize':'7'}
        f.edge(aut.q[edges].name, aut.q[edges].name, label = 'a, ..., z, A, ..., Z, 0, ..., 9')
    edges += 1
    