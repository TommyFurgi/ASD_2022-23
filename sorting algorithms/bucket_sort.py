def insertion_sort(A):
    n=len(A)
    for i in range(n):
        najm=i
        for j in range(i+1,n):
            if A[j]<A[najm]:
                najm=j

        A[najm],A[i]=A[i],A[najm]
    return A

def bucket_sort(A,a,b): # valurs in range <a,b>
    n=len(A)
    for i in range(n):
        A[i]-=a

    k=b-a+1
    res=[[] for _ in range(n)]
    for i in range(n):
        res[int(n*A[i]/k)].append(A[i])



    for i in range(n):
        insertion_sort(res[i])
    

    B=[]
    for i in range(n):
        B+=res[i]
        
    for i in range(n):
        B[i]+=a

    return B

tab=[2,6,3,4,7,10,4,2,9,10]
tab=bucket_sort(tab,2,10)
print(tab)