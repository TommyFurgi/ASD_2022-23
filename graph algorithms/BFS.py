# breadth-first search

from collections import deque

def bfs(G): # O(E+V) adjacency list
    n=len(G)
    visit=[False]*n
    visit[0]=True
    q=deque()
    q.append(0)
    while len(q):
        u=q.popleft()
        for i in G[u]:
            if not visit[i]:
                visit[i]=True
                q.append(i)


def bfs2(G): # O(V^2) adjacency matrix
    n=len(G)
    visit=[False]*n
    visit[0]=True
    q=deque()
    q.append(0)
    while len(q):
        u=q.popleft()
        for i in range(n):
            if not visit[i] and G[u][i]:
                visit[i]=True
                q.append(i)

