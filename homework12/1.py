class Graph:
    def __init__(self,mat,unconn=0):
        vnum=len(mat)
        self._mat=[mat[i][:] for i in range(vnum)]
        self._unconn=unconn
        self._vnum=vnum
    def vertex_num(self):
        return self._vnum
    def add_edge(self,vi,vj,val=1):
        self._mat[vi][vj]=val
    def get_edge(self,vi,vj):
        return self._mat[vi][vj]
    def out_edges(self,vi):
        return self._out_edges(self._mat[vi],self._unconn)
    @staticmethod
    def _out_edges(row,unconn):
        edges=[]
        for i in range(len(row)):
            if row[i]!=unconn:
                edges.append((i,row[i]))
        return edges



def travelsal(graph,point,depth,end):
    min_depth=1000
    n=graph.vertex_num()
    mark=[]
    for i in range(n):
        mark.append(0)
    if point==end:  #起点=终点
    #    if depth<min_depth:
        min_depth=0
    #for vi,vj in graph.out_edges(point):
    #    travelsal(graph,vj,depth+1,end)
    mark[start]=1
    q=[(start,0)]
    while len(q)!=0:
        point,depth=q.pop(0)
        for vi,vj in graph.out_edges(point):
            if mark[vj]!=1:
                if vj==end:
                    min_depth=depth+1
                    return min_depth
                mark[vj]=1
                q.append(vj,depth+1)
    return 0

in_=input().split()
n=int(in_[0])
m=int(in_[1])
mat=[]
for i in range(n):
    mat.append([])
    for j in range(n):
        mat[i].append(0)
        
graph=Graph(mat)
for i in range(m):
    in_=input().split()
    graph.add_edge(int(in_[0])-1,int(in_[1])-1)
    
in_=input().split()
start=int(in_[0])-1
end=int(in_[1])-1

print(travelsal(graph,start,0,end))








