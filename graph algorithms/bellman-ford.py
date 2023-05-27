# najkrotsza sciezka w grafie skierowanym z ujemnymi wagami

def bellman_ford(G,s,t): # O(VE) G-list of edges
    n=len(G)
    dist=[float('inf')]*n
    dist[s]=0
    T=[]
    for i in range(n):
        for j,k in G[i]:
            T.append((i,j,k))

    for k in range(n-1):
        for i,j,l in T:
            if dist[j]>dist[i]+l:
                dist[j]=dist[i]+l

    for i,j,l in T:
        if dist[j]>dist[i]+l:
            return None # istnieje cykl o ujemnej wadze
        
    return dist[t]
