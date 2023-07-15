# Given list of values. We play a game against the opponent and we always grab
# one value from either left or right side of our list of values. Our opponent
# does the same move. What is the maximum value we can grab if our opponent
# plays optimally, just like us.


def game(T):
    n=len(T)
    DP=[[0 for _ in range(n)] for _ in range(n)]

    suma=0
    for i in range(n):
        DP[i][i]=T[i]
        suma+=T[i]

    
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            if (i+j)%2==1:
                DP[i][j]=min(-1*T[i]+DP[i+1][j],-1*T[j]+DP[i][j-1]) 
            else:
                 DP[i][j]=max(T[i]+DP[i+1][j],T[j]+DP[i][j-1]) 


    return (suma-DP[0][n-1])//2 + DP[0][n-1]

V = [3, 8, 4, 5, 1, 7, 6]
print(game(V))


