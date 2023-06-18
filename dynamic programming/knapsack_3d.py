# knapsack prblem with height limit of knapsack

def knapsack(W,P,H,B,MaxH): # W- weights, P-values, H-heights,B-max weight
    n=len(W)
    T=[[[0 for _ in range(MaxH+1)] for _ in range(B+1)] for _ in range(n)] # T[item_number][free_pleace][free_height]


    for b in range(W[0],B+1):
        for h in range(H[0],MaxH+1):
            T[0][b][h]=P[0]

    for item in range(1, n):
        for place in range(B + 1):
            for height in range(MaxH + 1):
                T[item][place][height] = T[item - 1][place][height]
                if place >= W[item] and height >= H[item]:
                    T[item][place][height] = max(T[item][place][height], P[item] + T[item - 1][place - W[item]][height - H[item]])

    return T[n - 1][B][MaxH]


profit = [6, 10, 12]
weight = [1, 2, 3]
height = [3,4,5]
W = 5
H=8
print(knapsack(weight,profit,height,W,H))