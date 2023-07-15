# Given a rod of length n inches and a table of prices T[i] for i = [1, 2, ..., n].
# Determine the maximum revenue r[n] obtainable by cutting up the rod and selling
# the pieces.

def f(DP,i,T):
    if DP[i]!=-1:
        return DP[i]
    
    best=T[i-1]
    for j in range(i):
        best=max(best,f(DP,j,T)+T[i-j-1])

    DP[i]=best
    return best

def rod(T,n):
    DP=[-1]*(n+1)
    DP[0]=0
    return f(DP,n,T)


T = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 34, 34, 30, 49, 45, 43, 43, 52, 52]
n = 15
print(rod(T,n))