def floyd_warshall(G,a,b): # O(V^3) adjacency list
    n=len(G)
    T=[[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        T[i][i]=0

    for i in range(n):
        for j,k in G[i]:
            T[i][j]=k

    for t in range(n):
        for i in range(n):
            for j in range(n):
                 if T[i][j]>T[i][t]+T[t][j]:
                    T[i][j]=T[i][t]+T[t][j]
    return T[a][b]


def floyd_warshall2(G,a,b): # O(V^3) adjacency matrix
    n=len(G)
    T=[[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        T[i][i]=0

    for i in range(n):
        for j in range(n):
            if G[i][j]!=-1:
                T[i][j]=G[i][j]

    for t in range(n):
        for i in range(n):
            for j in range(n):
                 if T[i][j]>T[i][t]+T[t][j]:
                    T[i][j]=T[i][t]+T[t][j]
    return T[a][b]
