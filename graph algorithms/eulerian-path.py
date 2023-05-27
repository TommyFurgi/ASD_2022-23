def euler(G): # O(V^2) adjacency matrix
    def dfs(G,u):
        n=len(G)
        for i in range(n):
            if G[u][i]:
                G[u][i]=False
                G[i][u]=False
                dfs(G,i)
        res.append(u)

    res=[]
    dfs(G,0)
    return res[::-1]


def euler2(G): # O(EV) adjacency list
    def dfs(G,u):
        if len(G[u])>0:
            t=G[u].pop()
            G[t].remove(u)
            dfs(G,t)
        res.append(u)

    res=[]
    dfs(G,0)
    return res[::-1]