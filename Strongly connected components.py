#class for vertices
import math
import sys

class Node():
    def __init__(self,data):
        self.data=data
        self.isvisited=0
        self.color='white'
        self.group=None
        self.parent=[]
        self.d=None
        self.f=None
        
    def __str__(self):
        return self.data
    
class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


#input of adjacency edges
nodes = int(input().strip())
adj_mat = {}
vertices = [Node(i) for i in range(nodes)]
for i in range(nodes):
    edge = list(map(int,input().strip().split(" ")))
    adj_mat[i]=edge[:-1:]

time = 0

def DFS_Visit(u):
    global time
    time=time+1
    u.d=time
    u.color='gray'
    for v in adj_mat[u.data]:
        vertices[v].parent.append(u.data)
        if vertices[v].color=='white':
            DFS_Visit(vertices[v])
    u.color='black'
    time=time+1
    u.f=time    
    
for vertex in vertices:
    if vertex.color=='white':
        DFS_Visit(vertex)


#final time dict
ftime_arr = {}
for i in vertices:
    ftime_arr[i.f]=i.data

#new vertices sorted in decreasing finish time
new_vertex=[]
for key in sorted(ftime_arr.keys(),reverse=True):
    new_vertex.append(ftime_arr[key])
    
# reversed graph
reversed_graph={}
for i in range(nodes):
    reversed_graph[i]=[]

i=0
for a in adj_mat:
    for j in adj_mat[a]:
        reversed_graph[j].append(i)
    i+=1
reversed_graph

for i in range(nodes):
    vertices[i].isvisited=0
    
def DFS_Visit(u,a=None):
    u.isvisited=1
    for v in reversed_graph[u.data]:
        if vertices[int(v)].isvisited==1:
            pass
        else:
            a.append(v)
            DFS_Visit(vertices[v],a)

a={}
for vertex in new_vertex:
    if vertices[vertex].isvisited==0:
        corner = vertices[vertex].parent
        a[vertex]=[vertex]
        DFS_Visit(vertices[vertex],a[vertex])
    

#assigning group property to scc

for i in a:
    for j in a[i]:
        vertices[j].group=min(a[i])

grouplist=sorted(list(set(i.group for i in vertices)))

for i in a:
    for j in a[i]:
        vertices[j].group=grouplist.index(vertices[j].group)

finaldict = {}
for i in range(len(grouplist)):
    finaldict[i]=set()
for i in adj_mat:
    for j in adj_mat[i]:
        if(vertices[i].group!=vertices[j].group):
            finaldict[vertices[i].group].add(vertices[j].group)
    
sys.stdout.write(str(len(grouplist)))
sys.stdout.write("\n")
for i in range(len(grouplist)):
    if len(finaldict[i])==0:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(" ".join(str(x) for x in sorted(list(finaldict[i]))))
        sys.stdout.write(" -1\n")
