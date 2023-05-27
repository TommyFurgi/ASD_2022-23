# Tomasz Furgala

# zmieniam tablice E na liste sąsiedztwa z wagami
# sortuje tablice S quicksortem
# wykorzystuje heapq oraz algorytm dijikstry rozpatrujac najpierw poloczenia w tablicy S, a dopiero pozniej wierzcholki z tablicy sasiedztwa

# zlozonosc O(E)

from zad5testy import runtests
import heapq 

def change_tab(T,n):
    tab=[[] for _ in range(n)]
    for i in range(len(T)):
        a,b,time=T[i]
        tab[a].append((b,time))
        tab[b].append((a,time))

    return tab


def spacetravel( n, E, S, a, b ):
    visited=[float('inf')]*n
    tab=change_tab(E,n) # O(E)
    telemports=[False]*n
    for i in S:
        telemports[i]=True
    
    flag_teleports=False
    kolejka=[]
    visited[a]=0
    heapq.heappush(kolejka, (0,a))
    while len(kolejka)>0: # O(E)
        du,u= heapq.heappop(kolejka)
        if not flag_teleports and telemports[u]:
            flag_teleports=True
            for i in S:
                visited[i]=du
                heapq.heappush(kolejka,(visited[i],i))

        if du==visited[u]: 
            for i,time in tab[u]: 
                if visited[i]>(visited[u]+time):
                    visited[i]=(visited[u]+time)
                    heapq.heappush(kolejka,(visited[i],i))


    najm=visited[S[0]]
    for i in S:
        if visited[i]<najm:
            najm=visited[i]


    if visited[b]==float('inf'): # O(1)
        return None
    else:
        return visited[b]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )