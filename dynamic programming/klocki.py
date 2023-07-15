# rozpatrujemy spadajace klocki
# kazdy klocek oznacza przdzial <a,b>, 
# ile najmniej kloskow trzeba usunac aby wszystkie spadaly jeden na drugi tak by nie wystwaly

def upper(a,b):
    if a[0]<b[0] or a[1]>b[1]:
        return False
    return True


def f(DP,i,T,top):
        if i==0:
            top[0]=T[0]
            DP[i]=0
            return 0

        if DP[i]!=-1:
            return DP[i]

        best=1+f(DP,i-1,T,top)
        for j in range(i):
            if upper(T[i],top[j]):
                best=min(best,i-j-1+f(DP,j,T,top))
        best=min(best,i)
        
        DP[i]=best
        if best==1+f(DP,i-1,T,top):
            top[i]=top[i-1]
        else:
            top[i]=T[i]

        return best

def klocki(T):  

    n=len(T)
    DP=[-1]*n
    top=[None]*n
    f(DP,n-1,T,top)
    return DP[n-1]


T=[(1,5),(2,6),(1,3),(1,2)]
print(klocki(T))