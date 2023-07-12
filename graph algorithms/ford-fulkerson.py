from copy import deepcopy
from collections import deque

def path(parent,s,t,res):
    if t!=s:
        path(parent,parent[t],s,res)
        
    res.append(t)
    

def find_path(G,s,t):
    # BFS
    n=len(G)
    visit=[False]*n
    parent=[-1]*n
    q=deque()
    visit[s]=True
    q.append(s)
    while len(q):
        u=q.popleft()
        if u==t:
            break
        for i in range(n):
            if G[u][i]>0 and not visit[i]: 
                visit[i]=True
                parent[i]=u
                q.append(i)

    res=[]
    path(parent,s,t,res)
    return res


def min_weight(G,path):
    w=G[path[0]][path[1]]
    for i in range(1,len(path)-1):
        w=min(w,G[path[i]][path[i+1]])

    return w

def update_weights(G,path):
    w=min_weight(path)
    for i in range(len(path)-1):
        G[path[i]][path[i+1]]-=w
        G[path[i+1]][path[i]]+=w


def Ford_fulkerson(M,s,t): # M- adjacency matrix
    n=len(M)
    G=deepcopy(M)
    cnt=0
    my_path=find_path(G,s,t) 
    while my_path:
        cnt+=min_weight(my_path)
        update_weights(G,my_path)
        my_path=find_path(G,s,t)

    return cnt
