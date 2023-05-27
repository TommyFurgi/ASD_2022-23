def count_sort(A,n,index):
    C=[0]*26

    for i in range(n):
        C[ord(A[i][index])-97]+=1

    for i in range(1,26):
        C[i]+=C[i-1]

    B=[""]*n
    for i in range(n-1,-1,-1):
        B[C[ord(A[i][index])-97]-1]=A[i]
        C[ord(A[i][index])-97]-=1
    
    return B

def radix_sort(A):
    n=len(A)
    for i in range(len(A[0]) - 1, -1, -1):
        A=count_sort(A,n,i)
    
    return A

def sort_strings(A):
    n=len(A)
    maks=0
    for i in range(n):
        maks=max(maks,len(A[i]))

    buckets=[[] for _ in range(maks+1)]

    for i in range(n):
        buckets[len(A[i])].append(A[i])

    for i in range(maks+1):
        if len(buckets[i])!=0:
            buckets[i]=radix_sort(buckets[i])

    res=[]

    for i in range(maks+1):
        res+=buckets[i]

    return res

strings = ["zyb", "cfv", "ge", "u", "pr", "l", "cav", "xacdf", "bfq", "qsdf", "hjgd", "bgfp",
           "fasxc", "sdfgq", "bvcn", "q", "x", "ap", "ar", "hfg", "bs"]

print(sort_strings(strings))
