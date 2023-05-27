def bridges(G):  # O(VE) adjacency list
    def low(G,u,i,low_tab,timer):
        najm=timer[i]
        for j in G[i]:
            if j!=u:
                najm=min(najm,low_tab[j],timer[j])
        return najm

    def dfs(G,u):
        nonlocal time
        timer[u]=time
        time+=1
        visit[u]=True
        for i in G[u]:
            if not visit[i]:
                parent[i]=u
                dfs(G,i)
                low_tab[i]=low(G,u,i,low_tab,timer)

    n=len(G)
    visit=[False]*n
    low_tab=[float('inf')]*n
    timer=[0]*n
    parent=[-1]*n
    time=0
    for i in range(n):
        if not visit[i]:
            dfs(G,i)

    res=[]
    for i in range(n):
        if timer[i]==low_tab[i]:
            res.append((i,parent[i]))

    return res