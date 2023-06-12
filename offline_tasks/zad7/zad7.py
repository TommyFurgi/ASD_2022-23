# Tomasz Furgala

# algorytm iteracyjny O(n^2)
# algorymt polegana na obliczniu dla kazdej komnaty maksymalnej mozliwej drogi do[n-1][n-1]
# inicjalizuje 3 tablice nadajac wartosci -1 we wszystkich polach: T-zawiera koncowe dane, 
# Upper-przechwuje dane przechodzac od gory do dolu, Bottom-przechwuje dane przechodzac od dolu do gory
# algorytm polega na przechodzeniu po kazdej kolumnie od konca w taki sposob, ze najpierw zapisuje dane w tablicy Upper 
# maksimum z jednago pola na prawo i jednago pola od gory i dodaje to tego wartosc 1, nastepnie analogicznie dla tablicy 
# Bottom biorac pod uwage element jeden na prawo i element jeden na dol, na koniec zapisuje w tablicy 
# T[j][i]=max(Bottom[j][i],Upper[j][i])

from zad7testy import runtests

def maze( L ):

    n=len(L)
    Upper=[[-1 for _ in range(n)] for _ in range(n)]
    Bottom=[[-1 for _ in range(n)] for _ in range(n)]
    T=[[-1 for _ in range(n)] for _ in range(n)]

    T[n-1][n-1]=0
    for i in range(n-2,-1,-1):
        if L[i][n-1]=='#':
            break
        T[i][n-1]=T[i+1][n-1]+1

    T[n-1][n-1]=0

    for i in range(n-2,-1,-1):

        if L[0][i]!='#' and T[0][i+1]!=-1:
            Upper[0][i]=T[0][i+1]+1
            
        if i!=0:
            for j in range(1,n):
                a=max(Upper[j-1][i],T[j][i+1])
                if a!=-1 and L[j][i]!='#':
                    Upper[j][i]=1+a

        
        if L[n-1][i]!='#' and T[n-1][i+1]!=-1:
            Bottom[n-1][i]=T[n-1][i+1]+1
        for j in range(n-2,-1,-1):  

            a=max(Bottom[j+1][i],T[j][i+1])
            if a!=-1 and L[j][i]!='#':
                Bottom[j][i]=1+a

        for j in range(n):
            T[j][i]=max(Bottom[j][i],Upper[j][i])



    return T[0][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
