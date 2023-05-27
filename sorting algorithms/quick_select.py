# return value which would be on index q after sorting 

def partition(A,p,r):
    pivot=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=pivot:
            i+=1
            A[j],A[i]=A[i],A[j]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def select(A,k): # O(n)
    q=partition(A,0,len(A)-1)
    while q!=k:
        if q<k:
            q=partition(A,q+1,len(A)-1)
        else:
            q=partition(A,0,q-1)
        
    return A[q]