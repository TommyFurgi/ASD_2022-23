# Tomasz Furgala

# zlozonosc O(nm+mlogm)
# Algorytm  zachlanny,
# rozwiazanie polega na przechodzeniu o jedno pole w lewo i jezeli na tym polu jest plama paliwa to uzywam algorytmu bfs i zbieramy wszyskie polaczone 
# plamy, a sume zapisuje w odwroconym stosie. Przechodzac o jedno pole w prawo usuwam i paliwo z obecnie posiadanego, jezeli paliwo mi sie skonczy 
# to biore najwieksza wartosc ze stosu (najwieksza suma plam polaczonych ktore minalem i wczesniej nie zebralem).

from zad8testy import runtests
from collections import deque
from queue import PriorityQueue

def bfs(i,j,T):
    n=len(T)
    m=len(T[0])
    q=deque()
    q.append((i,j))
    suma=T[i][j]
    T[i][j]=0
    while len(q):
        x,y=q.popleft()
        for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0<=x+a<n and 0<=y+b<m and T[x+a][y+b]!=0:
                suma+=T[x+a][y+b]
                T[x+a][y+b]=0
                q.append((x+a,y+b))

    return suma

def plan(T):    
    n=len(T)
    m=len(T[0])

    paliwo=0
    plamy=PriorityQueue()

    cnt=0
    for i in range(m-1):
        if T[0][i]!=0:
            suma=bfs(0,i,T)
            plamy.put(suma*(-1))
        if paliwo==0:
            u=plamy.get()
            paliwo=u*(-1)
            cnt+=1
        paliwo-=1
    return cnt


runtests( plan, all_tests = True )

