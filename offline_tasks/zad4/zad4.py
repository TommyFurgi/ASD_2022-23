# Tomasz Furgala

# uzywam bfs, i szukam najkrotszych sciezek z s do t przy czym zapisuje wszystkie sciezki o tej najkrotszej dluosci, nastepnie szukam wierzchlkow wspolnych dla wszystkich tych zapisanych 
# sciezek i zwracam pierwszy wierzcholek wspolny i jego parent(i to jest ta szukana krawedz), jezeli nie ma tekiego wiecholka to zwracam None bo nie da sie jednoznacznie wskazac krawedzi,
# ktorej usuniecie spowoduje wydluzenie wszystkich najkrotszych sciezek

# V-liczba wierzcholkow, E-liczba krawedzi
# O(VE)

from zad4testy import runtests

def intersection(T): # szukamy czasci wspolnej naszy sciezek, 
    res=[]
    n=len(T)
    path_len=len(T[0])
    for i in range(path_len): # O(VE)
        for j in range(n-1):
            if T[j][i]!=T[j+1][i]:
                break
        else:
            res.append(T[0][i])
            break # interesuje nas tylko pierwszy punkt wspolny
    
    return res


def longer( G, s, t ):
    n=len(G) # ilosc wierzcholkow
    visted=[-1]*n # zapisuje w ktorej fali odwiedzono
    parent=[-1]*n
    kolejka=[]
    kolejka.append(s)
    visted[s]=0

    all_paths=[]
    i=0
    while i!=len(kolejka):  # dfs O(V+E)
        u=kolejka[i]
        i+=1
        for j in range(len(G[u])):
            if visted[G[u][j]]==-1:
                kolejka.append(G[u][j])
                visted[G[u][j]]=visted[u]+1
                parent[G[u][j]]=u

            if G[u][j]==t:
                if (visted[u]+1)==visted[G[u][j]]: # tu zapisuje wszystkie sciezki o najkrotszej dlugosci
                    path=[]
                    p=u
                    while p!=s:
                        path.append(p)
                        p=parent[p]
                    all_paths.append(path)
                else: # jesli istnieje juz sciezka o dlugosci wiekszej to nie ma sensu dalej sprawdzac BFSem bo wszystkie kolejne sciezki tez beda dluzsze od naszej najkrotszej
                    i=len(kolejka)
                    break

    if visted[t]==-1: # nie istnieje sciezka z s do t , len(all_paths)==0:
        return None
    elif len(all_paths)==1: # jest tylko jedna sciezka o takiej dlugosci
        return (parent[t],t) # mozna usunac dowolna krawdz z tej sciezki
    else:
        res=intersection(all_paths)
        if len(res)==0:
            return None
        else:
            return (parent[res[0]],res[0]) 
    
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )