# Tomasz Furgala
# O(EV)

# tworze tablice T ktora zawiera n-1 najmniejszych wagowo krawedzi z G, w T przechowuje posortowane krawedzie i sprawdzam czy tworza cykl 
# przy pomocy bfs jesli nie to zwracam sume krawedzi w T, a jeśli jest cykl to wyrzucam najmniejsza krawedz z T i dodaje do T kolejna 
# co do wagi z G tak by T byla dalej posortowana, jezeli jakis zbior krawdzi nie tworzy cyklu to jest to drzewo rozpinajace i zwracamy jego sume

from kol2testy import runtests
from collections import deque

def is_cycle(T): # BFS - V krawedzi wiec O(V+V)
    n=len(T)+1
    P=[[] for _ in range(n)]
    for i,j,t in T:
        P[i].append(j)
        P[j].append(i)

    q=deque()
    q.append(0)
    visit=[False]*n
    parent=[None]*n
    visit[0]=True
    while len(q):    
        u=q.popleft()
        for i in P[u]:
            if i!=parent[u]:
                if visit[i]:
                    return True
                parent[i]=u
                visit[i]=True
                q.append(i)

    for i in visit:
        if not i:
            return True
    return False


def sum(T):
    s=0
    for i,j,k in T:
        s+=k
    
    return s

def beautree(G):
    n=len(G) # liczba wierzcholkow
    E=[]
    for i in range(n): #O(E)
        for j,t in G[i]:
            if i<j:
                E.append((i,j,t))

    E.sort(key=lambda x:x[2]) # O(ElogE)

    T=[]
    for i in range(n-1): # n-1 l. krawedzi
        T.append(E[i])

    if not is_cycle(T):
        return sum(T)

    for i in range(n-1,len(E)): # O(EV)
        
        for j in range(1,len(T)): # O(V) tutaj przesuwam wszytkie krawedzie w T i wstawiam nowa na koniec
            T[j-1]=T[j]
        T[len(T)-1]=E[i]

        if not is_cycle(T): # O(V)
            return sum(T) #O(V)

    return None


runtests( beautree, all_tests = True )
