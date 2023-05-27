# Tomasz Furgala

# odwracam czesc wyrazow w tablicy
# sortuje tablice z uzyciem qs porownujac cale wyrazy
# na koniec zliczam ile maksymalnie mam tych samych wyrazow pod rzad w tablicy
# zlozonosc O(NlogN)

from zad3testy import runtests
from random import randint

def partition(T,p,r):
    k=randint(p,r)
    T[k],T[r]=T[r],T[k]
    pivot=T[r]
    i=p-1
    for j in range(p,r):
        if T[j]<pivot:
            i+=1
            T[i],T[j]=T[j],T[i]
    
    T[r],T[i+1]=T[i+1],T[r]
    return i+1

def quick_sort(A,p,r):
    while p<r: 
        q=partition(A,p,r)
        if (q-p)<(r-q):
            quick_sort(A,p,q-1)
            p=q+1
            
        else:
            quick_sort(A,q+1,r)
            r=q-1



def strong_string(T):
    # tu prosze wpisac wlasna implementacje
    n=len(T)
    for i in range(n): # O(N)
        if T[i]>T[i][::-1]:
            T[i]=T[i][::-1]
    
    quick_sort(T,0,n-1) # O(NlogN)

    najw=1
    dl=1
    for i in range(0,n): # O(N)
        if T[i]==T[i-1]:
            dl+=1
        else:
            najw=max(najw,dl)
            dl=1

    najw=max(najw,dl)

    return najw


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )

