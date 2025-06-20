class Vertex:
    def __init__(self,key):
        self.key=key
        self.neighbors={}
    
    def get_neighbor(self,other):
        return self.neighbors.get(other,None)

    def get_neighbors(self):
        return self.neighbors.keys()
    
    def get_key(self):
        return self.key
    
    def set_neighbor(self,other,weight=0):
        self.neighbors[other]=weight

class Graph:
    def __init__(self):
        self.vertices={}
    
    def set_vertex(self,key):
        self.vertices[key]=Vertex(key)

    def get_vertex(self,key):
        return self.vertices.get(key,None)

    def __contains__(self,key):
        return key in self.vertices
    
    def add_edge(self,from_vertex,to_vertex,weight=0):
        if from_vertex not in self.vertices:
            self.set_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.set_vertex(to_vertex)
        self.vertices[from_vertex].set_neighbor(to_vertex,weight)
    
    def get_vertices(self):
        return self.vertices.keys()
    
    def __iter__(self):
        return iter(self.vertices.values())

n,m=map(int,input().split())
graph=Graph()
for i in range(n):
    graph.set_vertex(i)
for i in range(m):
    a,b=map(int,input().split())
    graph.add_edge(a,b)
    graph.add_edge(b,a)
matrix=[]
for vertex in graph:
    row=[0]*n
    row[vertex.get_key()]=len(vertex.get_neighbors())
    for neighbor in vertex.get_neighbors():
        row[neighbor]-=1
    matrix.append(row)
for row in matrix:
    print(' '.join(map(str,row)))
    
