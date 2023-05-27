def merge_sort(A,p,r,letter):
    if p<r:
        mid=(p+r)//2
        merge_sort(A,p,mid,letter)
        merge_sort(A,mid+1,r,letter)

        i=p
        j=mid+1
        while j<=r and i!=j:
            if ord(A[j][letter])<ord(A[i][letter]):
                tmp=A[j]
                a=j
                while a!=i:
                    A[a]=A[a-1]
                    a-=1
                A[i]=tmp
                j+=1
            i+=1
        

def radix_sort(A): # values in table have the same length 
    n=len(A)
    dl=len(A[0])

    for i in range(dl-1,-1,-1):
        merge_sort(A,0,n-1,i)

    return A

T=['kra','art','kot','kit','ati','kil']
T=radix_sort(T)
print("result:", T)