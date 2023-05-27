# MST - Minimum spanning tree

from queue import PriorityQueue

def prima(G): # O(ElogV) adjacency list
    n=len(G)
    parent=[None]*n
    edge=[float('inf')]*n
    edge[0]=0
    q=PriorityQueue()
    q.put((0,0))
    while not q.empty():
        du,u=q.get()
        if du==edge[u]:
            for i,j in G[u]:
                if i!=parent[u] and j<edge[i]:
                    edge[i]=j
                    parent[i]=u
                    q.put((j,i))

    res=[]
    for i in range(1,n):
        res.append((parent[i],i,edge[i]))

    return res