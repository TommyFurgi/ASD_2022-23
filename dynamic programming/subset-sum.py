# Given a set of non-negative integers, and a value summary. Find if there is
# a subset of the given set with sum equal to given sum.


def sum(T,suma):
    def f(DP,i,suma,parent):
        if i<0 or suma<0:
            return float('inf')
        
        if suma==0:
            return 0

        if DP[i][suma]!=-1:
            return DP[i][suma]
        
        # best=min(f(DP,i-1,suma), 1+f(DP,i-1,suma-T[i]))
        # DP[i][suma]=best
        # return best
        if f(DP,i-1,suma,parent)<1+f(DP,i-1,suma-T[i],parent):
            parent[i][suma]=((i-1,suma))
            DP[i][suma]=f(DP,i-1,suma,parent)
        else:
            parent[i][suma]=((i-1,suma-T[i]))
            DP[i][suma]=1+f(DP,i-1,suma-T[i],parent)
        
        return DP[i][suma] 

    n=len(T)
    DP=[[-1 for _ in range(suma+1)] for _ in range(n)]
    parent=[[None for _ in range(suma+1)] for _ in range(n)]
    f(DP,n-1,suma,parent)
    
    if DP[n-1][suma]==float('inf'):
        return []


    res=[]
    a,b=n-1,suma
    while parent[a][b]!=None:
        curr1,curr2=parent[a][b]
        if b-curr2!=0:
            res.append(b-curr2)
        
        a,b=curr1,curr2

    return res[::-1]
    # return DP[n-1][suma]


D = [14, 5, 19, 3, 20, 14, 12, 7, 1]
summary = 70
print(sum(D,summary))