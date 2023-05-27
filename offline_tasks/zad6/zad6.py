# Tomasz Furgala

# zlozonosc O(En)
# tworze graf dwudzielny gdzie zbior A to maszyny a zbior B to pracownicy, dodatkowo dodaje dwa wierzcholki gdzie jeden jest polaczony z kazdym
# elementem zbioru, a drugi z kazdym elementem zb B,
# uzywam algorytmu Forda-Fulkersona odpalanja maksymalnie n razy dfsa szuakjac mozliwej sciezki w grafie(krawedzie maja wage 1)

from zad6testy import runtests
from collections import deque

def DFS(G,s,t):
    n=len(G)
    visited=[False for _ in range(n)]
    parent=[-1 for _ in range(n)]
    visited[s]=True
    stack=deque()
    stack.append(s)
    while len(stack): # O(E)
        u=stack.pop()
        
        if u==t:
            break

        for i in G[u]:
            if not visited[i]:
                parent[i]=u
                visited[i]=True
                stack.append(i)


    if visited[t]: # O(E)
        res=[]
        k=t
        while k!=s: 
            if k!=t and parent[k]!=s:
                G[k].append(parent[k])

            for i in range(len(G[parent[k]])-1,-1,-1):
                if G[parent[k]][i] == k:
                    G[parent[k]][i],G[parent[k]][len(G[parent[k]])-1]=G[parent[k]][len(G[parent[k]])-1],G[parent[k]][i]
                    G[parent[k]].pop()
                    break

            res.append(k)
            k=parent[k]
        res.append(s)
        return res[::-1]

    return []


def Ford_furkerson(G,s,t):
    cnt=0
    path=DFS(G,s,t) #O(E)
    while path: # O(En)
        cnt+=1
        path=DFS(G,s,t) #O(E)

    return cnt


def binworker( M ):
    n=len(M)
    start=2*n
    last=2*n+1


    G=[[last] for _ in range(n)]

    for i in range(n):
        G.append(M[i])

    start_tab=[i for i in range(n,start)]
    G.append(start_tab)
    G.append([])
    
    return Ford_furkerson(G,start,last)

    

runtests( binworker, all_tests = True )
