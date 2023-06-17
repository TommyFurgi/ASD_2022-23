# knapsack problem, but the elements are liquids

def knapsack_greedy(W,P,B): # W- weights, P-values, B-max weight

    n=len(W)
    K=[0 for i in range(n)] # P[i]/W[i]

    for i in range(n):
        K[i]=(P[i]/W[i],W[i],P[i])

    K.sort(key=lambda x: x[0], reverse=True)
    result=0
    for v_per_w,weight,value in K:
        if weight<=B:
            result+=value
            B-=weight
        else:
            result+=v_per_w*B
            B=0
            return result
        
    return result

profit = [60, 100, 120]
weight = [10, 25, 30]
W = 40
print(knapsack_greedy(weight,profit,W))