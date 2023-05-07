# Tomasz Furgala

# zmieniam tablice E na liste sąsiedztwa z wagami
# sortuje tablice S quicksortem
# wykorzystuje heapq oraz algorytm dijikstry rozpatrujac najpierw poloczenia w tablicy S, a dopiero pozniej wierzcholki z tablicy sasiedztwa

# zlozonosc O(ElogV + V^3)

from zad5testy import runtests
from random import randint
import heapq 

def change_tab(T,n):
    tab=[[] for _ in range(n)]
    for i in range(len(T)):
        a,b,time=T[i]
        tab[a].append((b,time))
        tab[b].append((a,time))

    return tab

def bin_search(T,val):
    n=len(T)
    lewy=0
    prawy=n-1
    while lewy<=prawy:
        mid=(lewy+prawy)//2
        if T[mid]==val:
            return True
        elif T[mid]<val:
            lewy=mid+1
        else:
            prawy=mid-1
    
    return False

def partition(A,p,r):
    idx=randint(p,r)
    A[r],A[idx]=A[idx],A[r]
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def quick_sort(A,p,r):
    while p<r:
        q=partition(A,p,r)
        quick_sort(A,p,q-1)
        p=q+1


def spacetravel( n, E, S, a, b ):
    visited=[float('inf')]*n
    tab=change_tab(E,n) # O(E)
    quick_sort(S,0,len(S)-1) # O(V log V)
    kolejka=[]
    visited[a]=0
    heapq.heappush(kolejka, (0,a))
    while len(kolejka)>0: # O(ElogV + V^3)
        du,u= heapq.heappop(kolejka)
        if du==visited[u]: #O(EV+V^2 log V)
            if bin_search(S,u): # O(V log V)
                for i in S: #O(V)
                    if visited[i]>visited[u]:
                        visited[i]=visited[u]
                        heapq.heappush(kolejka, (du,i))
            for i,time in tab[u]: #O(E)
                if visited[i]>(visited[u]+time):
                    visited[i]=(visited[u]+time)
                    heapq.heappush(kolejka,(visited[i],i))

    if visited[b]==float('inf'): # O(1)
        return None
    else:
        return visited[b]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )