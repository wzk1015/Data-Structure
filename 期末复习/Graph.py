from Stack import SStack
from import PrioQueue
class AdjGraphError(TypeError):    
    pass 
class Graph: # basic graph class, using adjacent matrix邻接矩阵
    def __init__(self, mat, unconn = 0):        
        vnum1 = len(mat)        
        for x in mat:            
            if len(x) != vnum1: # Check square matrix            
                raise ValueError("Argument for 'GraphA' is wrong.")        
            self.mat = [mat[i][:] for i in range(vnum1)]       
        self.unconn = unconn        
        self.vnum = vnum1    
    def vertex_num(self):        
        return self.vnum    
    def add_edge(self, vi, vj, val = 1):       
        assert 0 <= vi < self.vnum and 0 <= vj < self.vnum        
        self.mat[vi][vj] = val
    def add_vertex(self):        
        raise AdjGraphError( "Adj Matrix does not support 'add_vertex'")    
    def get_edge(self, vi, vj):        
        assert 0 <= vi < self.vnum and 0 <= vj < self.vnum       
        return self.mat[vi][vj]    
    def out_edges(self, vi):        
        assert 0 <= vi < self.vnum        
        return self._out_edges(self.mat, vi, self.unconn)    
    @staticmethod    
    def _out_edges(mat, vi, unconn):        
        edges = []        
        row = mat[vi]        
        for i in range(len(row)):            
            if row[i] != unconn:               
                edges.append((i, row[i]))        
        return edges    
    def __str__(self):        
        return "[\n" + "\n".join(map(str, self.mat)) + "\n]"+ "\nUnconnected: " + str(self.unconn)

#深度优先搜索（非递归）
def DFS(graph, v0):    
    vnum = graph.vertex_num()    
    visited = [0]*vnum    
    visited[v0] = 1    
    DFS_seq = [v0]    
    st = SStack()    
    st.push((0, graph.out_edges(v0)))    #下次应访问edge[i]
    while not st.is_empty():       
        i, edges = st.pop()        
        if i < len(edges):            
            v, e = edges[i]            
            st.push((i+1, edges))            
            if visited[v] == 0: # unvisited node                
                DFS_seq.append(v)                
                visited[v] = 1                
                st.push((0, graph.out_edges(v)))    
    return DFS_seq

#Prim法求最小生成树
def Prim(graph):    
    vnum = graph.vertex_num()    
    mst = [None]*vnum   #非None代表已进入U，值代表该点连接的边和权重
    cands = PrioQueue([(0, 0, 0)]) # 保存候选边
    count = 0    
    while count < vnum and not cands.is_empty():
        w, u, vmin = cands.dequeue()    #最小候选边       
        if mst[vmin]: 
            continue      #虽然入队是v不在U中，但出队时可能已在U中，需检查
        mst[vmin] = ((u, vmin), w)  #存入U中新顶点及权值
        count += 1        
        for v, w in graph.out_edges(vmin): #看是否有从vmin出发到达V-U顶点的边,w为权重
            if not mst[v]: #v在U-V，把v-vmin入队
                cands.enqueue((w, vmin, v))    
    return mst

#Kruskal法求最小生成树
def Kruskal(graph):    
    vnum = graph.vertex_num()    
    reps = [i for i in range(vnum)]    
    mst, edges = [], []    
    for vi in range(vnum): # put all edges into a list        
        for v, w in graph.out_edges(vi):            
            edges.append((w, (vi, v)))  
    edges.sort()
    
    for w, e in edges:        
        if reps[e[0]] != reps[e[1]]:            
            mst.append((e, w))            
            if len(mst) == vnum-1: 
                break            
            rep, orep = reps[e[0]], reps[e[1]]            
            for i in range(vnum):                
                if reps[i] == orep: 
                    reps[i] = rep    
    return mst 

def dijkstra_shortest_paths(graph, v0):    
    vnum = graph.vertex_num()    
    assert 0 <= v0 < vnum    
    paths = [None]*vnum    
    count = 0    
    cands = PrioQueue([(0, v0, v0)])    
    while count < vnum and not cands.is_empty():        
        plen, u, vmin = cands.dequeue()        
        if paths[vmin]: 
            continue        
        paths[vmin] = (u, plen)        
        for v, w in graph.out_edges(vmin):            
            if not paths[v]:                
                cands.enqueue((plen + w, vmin, v)) 
                #与Prim不同：优先队列依据是到v0的路径最短而不是到整个U的路径最短   
        count += 1   
    return paths

   
b=[[1 for i in range(10)] for i in range(10)]
a=Graph(b)
print(a)
    
    
    
    
    
    
    
    