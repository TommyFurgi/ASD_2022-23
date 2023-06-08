# ile najwiecej przedzialow mozemy wybrac tak by wybrane na siebie nie nachodzily (moga nachodzic koncami)

def fun(P):
    if len(P)<2:
        return len(P)
    
    P.sort(key=lambda x: x[1])
    print(P)
    cnt=1
    first=P[0]
    point=first[1]

    for T in P:
        if T[0]>=point:
            cnt+=1
            point=T[1]
    
    return cnt
          

P=[[0, 5], [4, 10], [8, 15], [13, 18], [16, 20], [2, 10]]
print(fun(P))