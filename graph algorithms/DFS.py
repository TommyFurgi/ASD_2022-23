# depth-first search

def dfs(G): # O(E+V) adjacency list
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


def dfs2(G): # O(V^2+V) adjacency matrix
    def dfs_visit(G,u):
        n=len(G)
        visit[u]=True
        for i in range(n):
            if not visit[i] and G[u][i]:
                dfs_visit(G,i)
        res.append(u)

    n=len(G)
    visit=[False]*n
    res=[]
    for i in range(n):
        if not visit[i]:
            dfs_visit(G,i)

    return res[::-1]

