# prom ma dwa pokladu, ile najwiece pojadow moze wjechac na prom jezeli wjezdzaja w o odpowiedniej kolejnosci

def prom(T,l):
    def f(DP,i,l1,l2):
        if l1<0 or l2<0:
            return -1*float('inf')
        
        if i>=len(T):
            return 0
        
        if DP[l1][l2]!=-1:
            return DP[l1][l2]


        best=max(0,1+f(DP,i+1,l1-T[i],l2),1+f(DP,i+1,l1,l2-T[i]))
        DP[l1][l2]=best
        return best 
    
    n=len(T)
    DP=[[-1 for _ in range(l+1)] for _ in range(l+1)]
    f(DP,0,l,l)
    return DP[l][l]

T = [5, 6, 1, 3, 2, 4, 3, 5]
l = 10
print(prom(T,l))