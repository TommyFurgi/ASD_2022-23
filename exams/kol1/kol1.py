# Tomasz Furgala

# zlozonosc O(np)
# petla wykonuje n-p+1 przejsc bo tyle przedzialow rozpatrujemy (z tylu elemnetu sklada sie szukana przez nas suma), 
# w kazdym przejsciu do tablicy C zapisuje  przedzial ktory bedziemy przeszukiwac, 
# a nastepnie wywoluje funkcje quick_select do znalezienia k-tego najwiekszego elemnetu tej tablicy
# brute force 

from kol1testy import runtests
from random import randint


def partition(A,p,r):
    x=randint(p,r)
    A[x],A[r]=A[r],A[x]
    pivot=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]>pivot:
            i+=1
            A[i],A[j]=A[j],A[i]

    A[r],A[i+1]=A[i+1],A[r]
    return i+1

def quick_select(A,p,r,k):
    while True:
        q=partition(A,p,r)
        if q==k:
            return A[k]
        elif q<k:
            p=q+1
        else:
            r=q-1


def ksum(T, k, p):
    n=len(T)
    sum=0
    for i in range(n-p+1): # O(n-p+1) czyli okolo O(n)
        C=[0]*p
        ind=0
        for j in range(i,i+p): # O(p)
            C[ind]=T[j]
            ind+=1
        

        sum+=quick_select(C,0,p-1,k-1) # O(p log p)


    return sum



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )


