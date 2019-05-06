from graphviz import Digraph
#https://graphviz.readthedocs.io/en/stable/manual.html
#https://renenyffenegger.ch/notes/tools/Graphviz/examples/index

# f = Digraph('finite_state_machine', filename='fsm.gv')
# f.attr(rankdir='LR', size='7')

# f.attr('node', shape='doublecircle')
# f.node('q2')

# f.attr('node', shape='circle')
# f.edge('q1', 'q2', label='a,b')

# f.attr('node', shape='none')
# f.edge('', 'q1')

# f.view()

###################

f = Digraph('finite_state_machine', filename='fsm.gv')
f.attr(rankdir='LR', size='7')

name = str(input())

f.attr('node', shape='circle')
f.edge(name, 'q2', label='a,b')

f.attr('node', shape='none')
f.edge('', name)

f.view()