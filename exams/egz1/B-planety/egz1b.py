from egz1btesty import runtests

# tworze tablice programowania dynamicznego N na (B+1) i wywoluje funkcje f(i,b) - minimalny koszt majac b paliwa oraz bedac na 
# planecie 'i' zeby dotrzec to planety n-1
# zapisuje warunki konca oraz dla kazdego wywolania funkcji szukam optymalnej kosztowo drogi
# uruchiamiam dwie petle(pierwsza odpowiada temu ile tankuje, druga do jakiej plany podrozujemy)
# sprawdzam na koniec mozliwosc skorzystania z telportacji
# zapisuje wynik best w tablicy DP

# zlozonosc O(nE^2)


def planets( D, C, T, E ):
    def f(i,b): # minimalny koszt majac b paliwa oraz bedac na planeci 'i' zeby dotrzec to planety n-1
        nonlocal E
        if b<0 or b>E:
            return float('inf')
        
        if i==n-1:
            return 0
        
        if DP[i][b]!=-1:
            return DP[i][b]
        

        best=float('inf')
        for j in range(i+1,n):
            k=abs(D[i]-D[j])-b
            for t in range(max(0,k),E-b+1):
                best=min(best,t*C[i]+f(j,b+t-abs(D[i]-D[j])))

        if b==0 and T[i][0]>i: # sprawdzam mozliwosc skorzystania z teleportacji
            best=min(best,T[i][1]+f(T[i][0],0))

        DP[i][b]=best
        return best


    n=len(D)
    DP=[[-1 for _ in range(E+1)] for _ in range(n)]
    res=f(0,0) # wywoluje dla (0,0) bo startujemy z planety 0 i mamy 0 paliwa na start
    return res


runtests( planets, all_tests = True )
