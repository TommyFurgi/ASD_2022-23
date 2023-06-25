# Tomasz Furgala

# O(n^2)
# zamieniam dane tak by tworzyly krotki(indeks pod ktorym jest paking,cena)
# tworze tablice gdzie pierwszy wiersz zawiera minimalny koszt by dojechac z i-tego indeksu do konca trasy gdy kierowca moze jecach maksymalnie L trasy 
# pomiedzy pakingami, drugi wiersz zawiera minimalny koszt by dojechac z i-tego indeksu do konca gdy kierowca jedzie z itego indeksu 2L trasy,
# trzeci minmalny koszt aby dojechac z poczatku do itego indeksu
# stosujac programowanie dynamiczne uzupelniam kolejne wiersze w tablicy i na koniec szukam min(cache[1][i]+cache[2][i]+p[i][1])

from zad9testy import runtests

def min_cost( O, C, T, L ):

    n=len(O)
    p=[None for _ in range(n)] 
    for i in range(n):
        p[i]=(O[i],C[i])
    
    p.append((0,0))
    p.append((L,0))
    n+=2

    p.sort(key=lambda x: x[0])
    cache=[[float('inf') for _ in range(n)] for _ in range(3)]
    cache[2][0]=0
    cache[0][n-1]=0
    cache[1][n-1]=0

    for i in range(n-2,-1,-1):
        u,cu=p[i]
        best=float('inf')
        best2=float('inf')
        for j in range(i+1,n):
            a,b=p[j]
            if a-u<=T:
                best=min(best,b+cache[0][j])
            elif a-u<=2*T:
                best2=min(best2,b+cache[0][j])
            else:
                break
        best2=min(best,best2)
        cache[1][i]=best2
        cache[0][i]=best

    result=cache[1][0]
    for i in range(1,n):
        u,cu=p[i]
        best=float('inf')
        for j in range(i-1,-1,-1):
            a,b=p[j]
            if u-a<=T:
                best=min(best,b+cache[2][j])

        cache[2][i]=best  
        result=min(result,cache[1][i]+cache[2][i]+p[i][1])
    
    
    return result


runtests( min_cost, all_tests = True )
