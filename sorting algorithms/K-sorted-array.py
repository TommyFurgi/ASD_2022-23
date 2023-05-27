def left(i): return 2*i+1
def right(i): return 2*i+2
def parent(i): return (i-1)//2

def heapify(A,n,i): #log k
    l=left(i)
    r=right(i)
    max_ind=i
    if l<n and A[max_ind]>A[l]:
        max_ind=l
    if r<n and A[max_ind]>A[r]:
        max_ind=r

    if max_ind!=i:
        A[max_ind],A[i]=A[i],A[max_ind]
        heapify(A,n,max_ind)

def build_heap(A):
    n=len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,n,i)

def k_sorted_array(A,k): # nlogk
    n=len(A)

    B=[0]*(k+1)
    for i in range(k+1):
        B[i]=A[i]

    res=[0]*n
    build_heap(B)
    for i in range(n): #nlogk
        res[i]=B[0]
        if i+k+1<n:
            B[0]=A[i+k+1]
        else:
            B[0]=float('inf')
        
        heapify(B,k+1,0)

    return res

T=[4, 3, 1, 2, 7, 5, 6, 9, 8, 10]
k=3
print(k_sorted_array(T,k))