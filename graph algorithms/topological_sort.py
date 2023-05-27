def topological_sorting(G): # O(E+V)
    def dfs_visit(G,u):
        visit[u]=True
        for i in G[u]:
            if not visit[i]:
                dfs_visit(G,i)
        res.append(u)

    n=len(G)
    visit=[False]*n
    res=[]
    for i in range(n):
        if not visit[i]:
            dfs_visit(G,i)
            
    return res[::-1]