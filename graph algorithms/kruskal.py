# MST - Minimum spanning tree

def kruskal(G): # O(E log V)
    def find(a,parent):
        if parent[a]!=a:
            parent[a]=find(parent[a],parent)

        return parent[a]

    def union(i,j,t,res,x,y):
        parent[y]=x
        parent[j]=x
        res.append((i,j,t))

    n=len(G)
    parent=[i for i in range(n)]
    E=[]
    for i in range(n):
        for j,t in G[i]:
            if i<j:
                E.append((i,j,t))

    E.sort(key=lambda x:x[2])
    res=[]
    for i,j,t in E:
        x=find(i,parent)
        y=find(j,parent)

        if x!=y:
            union(i,j,t,res,x,y)
        
        if len(res)==(n-1):
            break

    return res