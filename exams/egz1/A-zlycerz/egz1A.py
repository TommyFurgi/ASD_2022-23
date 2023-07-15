from egz1Atesty import runtests
from queue import PriorityQueue

# uruchamiam algorytm dijkstry 2 razy szukajac sciezki z s do kazdego innego wierzcholka oraz 
# potem drugi z t do kazdego innego z warunkami jakie panuja po napadzie(czyli lapowka + 2*koszt drogi)
# wyniki zapisuje w tablicach

# nastepnie szukam takiego zamku ktorego (obrabowanie - minimalny koszt drogi z s - minimalny koszt drogi z t) jest najwiekszy
# wynik mnoze razy -1 (nie wiem dlaczego bo tresc jest dziwnie napisana, ale wtedy algorytm dziala)
# 
# zlozonosc O(E*logV) bo taka jest lozonosc algorytmu dijkstry dla takiej repzereznacji grafu
# E to okolo V^2 (E<V^2)
# zatem  O(V^2logV)

def dijkstra(G,a,r,mnoznik): # r to lapowka, mnoznik zalezy czy jestesmy przed czy po napadzie
  n=len(G)
  v=[float('inf')]*n
  v[a]=0
  q=PriorityQueue()
  q.put((0,a))
  while not q.empty():
    du,u=q.get()
    if du==v[u]:

      for i,j in G[u]:
        if v[i]>du+j*mnoznik+r:
          v[i]=du+j*mnoznik+r
          q.put((du+j*mnoznik+r,i))

  return v

def gold(G,V,s,t,r):
  n=len(G)
  przed=dijkstra(G,s,0,1) # lapowka - 0 , mnoznik -1 
  po_napdzie=dijkstra(G,t,r,2) # lapowka - r , mnoznik - 2 

  best=-float('inf') 
  for i in range(n): # szukam optymalnego zamku do okradniecia uwzgledniajac koszty drogi przed i po
    best=max(best,V[i]-przed[i]-po_napdzie[i])
  
  return best*(-1) # nie wiem czemu *(-1), nie rozumiem do konca tresci, ale wtedy program zwraca dobre wyniki


runtests( gold, all_tests = True )
