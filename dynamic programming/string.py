# Dana jest tablica string S[n] będąca zbiorem słów oraz ciąg znaków string t. Napisz funkcję, która
# znajdzie najmniejszy taki ciąg słów ze zbioru S, aby po ich złączeniu otrzymać tekst t.

def f(DP,i,S,t,parent):
    if i<0:
        return 0
    
    if DP[i]!=-1:
        return DP[i]
    
    best=float('inf')
    for j in S:
        p=len(j)
        if i-p+1>=0 and j==t[i-p+1:i+1]:
            if best>1+f(DP,i-p,S,t,parent):
                best=1+f(DP,i-p,S,t,parent)
                parent[i]=i-p

    DP[i]=best
    return best

def res(i,parent,tab,t):
    if i<0:
        return tab
    
    j=parent[i]
    res(j,parent,tab,t)
    
    tab.append(t[j+1:i+1])
    return tab

def string(S,t):
    n=len(t)
    DP=[-1]*n
    parent=[None]*n
    f(DP,n-1,S,t,parent)

    if DP[n-1]!=float('inf'):
        result=res(n-1,parent,[],t)
        return result
    return


S=["a","at","m","ca","aaa","mc","t"]
t="mcaaat"
# 3
print(string(S,t))