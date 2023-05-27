def counting_sort(T,a,b): # values in range <a,b>
    n=len(T)
    for i in range(n):
        T[i]-=a
    k=(b-a)
    C=[0]*(k+1)
    for i in range(n):
        C[T[i]]+=1

    for i in range(1,k+1):
        C[i]+=C[i-1]

    B=[0]*n

    for i in range(n-1,-1,-1):
        B[C[T[i]]-1]=T[i]+a
        C[T[i]]-=1

    return B

tab=[2,6,3,4,7,10,4,2,9,10]
tab=counting_sort(tab,2,10)
print(tab)