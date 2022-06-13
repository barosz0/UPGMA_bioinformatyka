import os
from pygraphviz import AGraph


def print_matrix(mat):
    for l in mat:
        print(l)


class Tree_node():
    def __init__(self) -> None:
        self.child = []
        self.dist = []
        self.name = ""
    
    def get_height(self):
        
        if len(self.child) == 1:
            return 0;
        else:
            return self.child[0].get_height() + self.dist[0]

node_nr = 0

def make_graph(tree:Tree_node,G):

    global node_nr
    
    if tree.name != '':
        pass
    elif node_nr == 0:
        tree.name = 'root'
        node_nr +=1
    else:
        tree.name = f'n{node_nr}'
        node_nr +=1


    if len(tree.child) >1:
        make_graph(tree.child[0],G)
        make_graph(tree.child[1],G)

        print(tree.name)

        G.add_edge(tree.name,tree.child[0].name, label = str(tree.dist[0]))
        G.add_edge(tree.name,tree.child[1].name, label = str(tree.dist[1]))
        
    
    return G

        

def find_min_dist(mat):
    i = 0

    size = len(mat)

    found = None
    index = None

    while i < size:
        j = i
        while j < size:
            if j!=i:
                if found is None:
                    found = mat[i][j]
                    index = [i,j]

                else:
                    if(mat[i][j] < found):
                        index = [i,j]
                        found = mat[i][j]

            j+=1
        i+=1
    
    return index

def group_levels(tree):
    if len(tree.child) == 1:
        return [[tree.name]]
    
    A = group_levels(tree.child[0])
    B = group_levels(tree.child[1])

    if len(A) < len(B):
        A, B = B, A
    
    for i in range(len(B)):
        A[i].extend(B[i])
    
    A.append([tree.name])

    return A
        


def merge_nodes(n1,n2,nodes,mat):

    new_node = Tree_node()

    new_node.child.append(nodes[n1])
    new_node.child.append(nodes[n2])



    
    dist1 = mat[n1][n2]/2 - new_node.child[0].get_height()
    dist1 = round(dist1,2)
    new_node.dist.append(dist1)

    dist2 = mat[n1][n2]/2 - new_node.child[1].get_height()
    dist2 = round(dist2,2)
    new_node.dist.append(dist2)


    # if(new_node.child[1].name=="e"):
    #     print(f"1 {mat[n1][n2]} {new_node.child[0].get_height()} {dist1}")
    #     print(f"2 {mat[n1][n2]} {new_node.child[1].get_height()} {dist2}")

    # if(new_node.child[0].name=="e"):
    #     print(f"1 {mat[n1][n2]} {new_node.child[0].get_height()} {dist1}")
    #     print(f"2 {mat[n1][n2]} {new_node.child[1].get_height()} {dist2}")
        

    c1 = len(nodes[n1].child)
    c2 = len(nodes[n2].child)

    #kolumna
    for i in range(len(mat)):
        if i!=n1 and i!=n2:
            dist = (mat[i][n1]*c1 + mat[i][n2])/(c1 + c2)

            mat[n1][i] = dist
            mat[i][n1] = dist



        

    nodes[n1] = new_node
    # Usuwanie nie potrzebnych node
    nodes.pop(n2) 

    mat.pop(n2)
    for l in mat:
        l.pop(n2)



def make_tree(mat, names = None, file = "tree.png"):
    print("Zaczynam")
    nodes = []

    for i in range(len(mat)):
        new_node = Tree_node()
        new_node.child.append(0)
        new_node.name = f"leaf_{i}"
        nodes.append(new_node)

    if names is not None and len(names) == len(nodes):

        for i in range(len(nodes)):
            nodes[i].name = names[i]
    
    # for n in nodes: print(n.child)
    while len(nodes)>1:
        indeks = find_min_dist(mat)
        merge_nodes(indeks[0],indeks[1],nodes,mat)
    
    
    G=AGraph(directed=True)

    make_graph(nodes[0],G)

    L = group_levels(nodes[0])

    for l in L:    
        NG = G.add_subgraph(l)
        NG.graph_attr['rank'] = 'same'


    G.layout(prog='dot')
    G.draw(file)  







if __name__ == "__main__":
    os.system("C:/Users/baros/miniconda3/python.exe main.py")