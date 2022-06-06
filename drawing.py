from cProfile import label
from pygraphviz import *

G=AGraph()
G=AGraph(directed=True)

G.add_edge("a","b",label = "123")

# G.write('ademo.dot')

G.layout(prog='dot')
G.draw("tree.png")