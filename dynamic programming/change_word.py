# We are given two strings string1 and string2 and below operations that can be
# performed on string1. Find minimum number of edits (operations) required to convert
# string1 into string2.
# 1. Insert
# 2. Remove
# 3. Replace
# All the above operations are of equal cost.

def change(w1,w2):
    n=len(w1)
    m=len(w2)
    DP=[[float('inf') for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        DP[i][0]=0

    for i in range(m+1):
        DP[0][i]=0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if w1[i-1]==w2[j-1]:
                DP[i][j]=DP[i-1][j-1]
            
            else:
                DP[i][j]=1+min(DP[i-1][j-1],DP[i-1][j],DP[i][j-1])

    return DP[n][m]

string1 = "abcdefg"
string2 = "azcefh"
print(change(string1,string2))


