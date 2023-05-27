# Tomasz Furgała 
# szukam indeks srodka palindronu poprzez porównanie indeksów o 1 mniejszego i o 1 wiekszego oraz sprawdzam czy palindron ma szanse być dluższym od najdłuższego dotąd znalezionego,
# jesli tak to porównuje kolejne indeksy na lewo i prawo od środka
# złożoność O(n^2)


from zad1testy import runtests

def ceasar( s ):
    # tu prosze wpisac wlasna implementacje

    najdl=1
    p=0
    for i in range(len(s)-2):
        if s[i]==s[i+2] and i-p>=0 and i+p+2<len(s) and s[i-p]==s[i+p+2]:
            a=i-1
            b=i+3
            dl=3
            while a>=0 and b<len(s) and s[a]==s[b]:
                a-=1
                b+=1
                dl+=2
            najdl=max(dl,najdl)
            p=(najdl-1)//2


    return najdl


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
