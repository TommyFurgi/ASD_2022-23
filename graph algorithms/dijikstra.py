# shortest path from s to t

from queue import PriorityQueue

def dijikstra(G,s,t): # O(ElogV) adjacency list
    n=len(G)
    dist=[float('inf')]*n
    q=PriorityQueue()
    dist[s]=0
    q.put((0,s))
    while not q.empty():
        du,u=q.get()
        if du==dist[u]:
            for i,j in G[u]:
                if dist[i]>du+j:
                    dist[i]=du+j
                    q.put((dist[i],i))

    return dist[t]


def dijikstra2(G,s,t): # O(V^2logV) adjacency matrix
    n=len(G)
    dist=[float('inf')]*n
    q=PriorityQueue()
    dist[s]=0
    q.put((0,s))
    while not q.empty():
        du,u=q.get()
        if du==dist[u]:
            for i in range(n):
                if dist[i]>du+G[u][i]:
                    dist[i]=du+G[u][i]
                    q.put((dist[i],i))

    return dist[t]
