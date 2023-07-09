# We are given an array of numbers that represent each coin. The number of coins we have are infinity,
# so we do not need to worry about how many coins are at our disposal. Then we are given an amount and
# asked to find how many ways can we make the change.

def f(DP,i,T,parent):
    if DP[i]!=float('inf'):
        return DP[i]
    
    best=float('inf')
    for j in range(len(T)):
        if T[j]<=i and best>1+f(DP,i-T[j],T,parent):
            best=1+f(DP,i-T[j],T,parent)   
            parent[i]=i-T[j]

    DP[i]=best
    return best

def ps(i,parent,T,res):
    a=parent[i]
    if a!=None:
        ps(a,parent,T,res)
        res.append(i-a)

    return res

def coin(T,money):
    DP=[float('inf')]*(money+1)
    parent=[None]*(money+1)
    T.sort()
    DP[0]=0

    f(DP,money,T,parent)
    res=[]
    res=ps(money,parent,T,res)
    return res

total_money = 11
coins = [1, 2, 10]
print(coin(coins, total_money))