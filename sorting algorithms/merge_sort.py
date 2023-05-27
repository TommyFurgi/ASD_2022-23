def merge_sort(A,p,r): # O(nlogn)
    if p<r:
        mid=(p+r)//2
        merge_sort(A,p,mid)
        merge_sort(A,mid+1,r)

        i=p
        j=mid+1
        while j<=r and i<j:
            if A[j]<A[i]:
                tmp=A[j]
                a=j
                while a<i:
                    A[a]=A[a-1]
                    a-=1
                A[i]=tmp
                j+=1
            i+=1
