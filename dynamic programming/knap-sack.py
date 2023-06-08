def knapsack(W,P,B): # W- weights, P-values, B-max weight
    n=len(W)
    F=[[0 for b in range(B+1)] for i in range(n)]
    for b in range(W[0],B+1):
        F[0][b]=P[0]

    for b in range(B+1):
        for i in range(1,n):
            F[i][b]=F[i-1][b]
            if b-W[i]>=0:
                F[i][b]=max(F[i][b],F[i-1][b-W[i]]+P[i])

    return F[n-1][B]

profit = [60, 100, 120]
weight = [10, 20, 30]
W = 50
print(knapsack(weight,profit,W))