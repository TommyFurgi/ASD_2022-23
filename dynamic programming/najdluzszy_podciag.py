# najdluzszy (niekoniecznie spojny) podciag w tablicy

def ps(A,P,i,res):
    if P[i]!=-1:
        ps(A,P,P[i],res)
    res.append(A[i])


def longest_substring(A):
    n=len(A)
    P=[-1]*n
    F=[1]*n
    for i in range(1,n):
        for j in range(i):
            if A[j]<A[i] and F[i]<F[j]+1:
                F[i]=F[j]+1
                P[i]=j

    res=[]
    index=n-1
    last_value=F[n-1]
    for i in range(n-1,-1,-1):
        if F[i]>last_value:
            index=i
            last_value=F[i]
    
    ps(A,P,index,res)
    return res

A=[2,1,4,3,1,5,2,7,8,3]
print(longest_substring(A))
