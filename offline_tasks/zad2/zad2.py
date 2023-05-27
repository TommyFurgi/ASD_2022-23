# Tomasz Furgala

# dla tablicy S = [1,7,3,4,1], mozemy brac elementy w kolejnych dniach w kolejnosci: 7,3,4 lub 4,3,7 lub 4,7,3... i zawsze suma bedzie wynosic tyle samo zatem, nie ma znaczenia 
# w jakiej kolejnosci bedziemy wybierac elementy, a znaczenie ma jedynie jakie to beda elementy. Lecz jak wezniemy np 1,7,3,4 to suma juz bedzie mniejsza wiec nie oplaca sie w tej
# sytuacji brac elementu 1. Na tej podstawie zauwazam ze oplacalne jest branie elemntow takich, ze w posotowanej nierosnaco tablicy warto brac tylko elmenty takie, ze S[i]>i

# wykorzystuje quicksorta do znalezienia takiego najmniejszego pivotu, ze S[i]>=i i wtedy wiem, ze elemnety na lewo od tego pivotu pomimo, ze sa nieposortowane to i tak zostana 
# wliczone do sumy i nie wazne w jakiej kolejnosci zawsze otrzymamy ten sam wynik wiec nie ma sensu ich sortowac, natomast elementy na prawo od pivotu tez sa nieposortowane,
# ale ich nawet nie bierzemy pod uwage.

# zlozonosc O(n logn)

from zad2testy import runtests
from random import randint

def partition(A,p,r):
    k=randint(p,r)
    A[k],A[r]=A[r],A[k]
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]>x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def quick_sort(A,p,r): # nlog n
    if p<r:
        q=partition(A,p,r)
        if A[q]<q:
            quick_sort(A,p,q-1)
        else:
            quick_sort(A,q+1,r)


def snow( S ):
    n=len(S)    
    snieg=0
    quick_sort(S,0,n-1)
    for i in range(n):
        if S[i]>i:
            snieg+=(S[i]-i)
        else:
            break
    
    return snieg

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
