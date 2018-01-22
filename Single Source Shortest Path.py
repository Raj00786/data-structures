class Vertices():
    def __init__(self,data):
        self.data = data
        self.d = 1000000
        self.pos = data


#input data

temp = list(map(int,raw_input().split()))
n = temp[0]
s = temp[1]
d = temp[2]
l = temp[3:]

vertexes = [Vertices(0)]
for i in range(1,n+1):
    vertexes.insert(i,(Vertices(i)))
    if i==s:
        vertexes[i].d=0
        
nodes = {}
for i in range(1,n+1):
        nodes[i] = []

        
#code for adjacency matrix of vertices
for i in range(n+1):
    deg = (i*l[1]+i*i*l[3])%d
    for j in range(1,deg+1):
        vertex = (i*l[0] + j*l[2]) % n
        vertex += 1
        weight = (i*l[4] + j*l[5]) % l[6]
        nodes[i].append([vertex,weight])

    
    
distances=vertexes[:]

def build_min(distances,size):
    for i in range(size//2,0, -1):
        min_heapify(distances,i,size)        

def min_heapify(distances,i,size):
    left = 2 * i
    right = 2 * i + 1
    smallest=i
    if(left < size and distances[left].d < distances[i].d):
        smallest = left
    else:
        smallest=i
    if(right < size and distances[right].d < distances[smallest].d):
        smallest=right
    if(smallest!=i):
        distances[i],distances[smallest]=distances[smallest],distances[i]
        
        distances[i].pos = i
        distances[smallest].pos = smallest
        
        min_heapify(distances,smallest,size)

        
def extract_min(distances):
    if len(distances)==2:
        return distances.pop()
    
    distances[1],distances[-1] = distances[-1],distances[1]
    emin = distances.pop()
    
    distances[1].pos = 1
    size=len(distances)
    min_heapify(distances,1,size)
    return emin

def decrease_key(distances,i):
    while i>1 and distances[i//2].d>distances[i].d:
        distances[i].pos = i//2
        distances[i//2].pos = i
        distances[i],distances[i//2] = distances[i//2],distances[i]
        i = i//2

build_min(distances,n)

def relax(u,v,w):
    if vertexes[v].d > vertexes[u].d + w:
        vertexes[v].d = vertexes[u].d + w
        decrease_key(distances,vertexes[v].pos)
        
#dijkstra
while len(distances)!=1:
    u = extract_min(distances)
    for adjvertex in nodes[u.data]:
        if vertexes[adjvertex[0]].pos >= 0 and u.data != adjvertex[0]:
            relax(u.data,adjvertex[0],adjvertex[1])
    u.pos = -100

            
for i in range(1,n+1):
    if vertexes[i].d==1000000:
        vertexes[i].d = -1

for i in range(1,n+1):
    print i,vertexes[i].d
