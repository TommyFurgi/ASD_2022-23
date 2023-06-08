# Travelling salesman problem 
# Given a list of cities and the distances between each pair of cities, 
# what is the shortest possible route that visits each city exactly once and returns to the origin city?

import math

def count_distance(city1, city2):
    x_distance = city1[0] - city2[0]
    y_distance = city1[1] - city2[1]
    return math.sqrt(x_distance**2 + y_distance**2)

def tsp(Points):
    n=len(Points)
    Points.sort(key=lambda x: x[1])
    D=[[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(1,n):
        x,y=Points[i]
        for j in range(i):
            a,b=Points[j]
            dist=math.sqrt((x-a)**2+(y-b)**2)
            D[i][j]=dist
            D[j][i]=dist


    F=[[float('inf') for _ in range(n)] for _ in range(n)]
    F[0][1]=D[0][1]
    minimum_distance = float('inf')
    for i in range(n-1):
        minimum_distance = min(minimum_distance, tspf(i, n-1, F, D) + D[i][n-1])
    return minimum_distance

def tspf(i,j,F,D):
    if F[i][j]!=float('inf'): return F[i][j]

    if i==j-1:
        best=float('inf')
        for k in range(j-1):
            best=min(best,tspf(k,j-1,F,D)+D[k][j])
        F[j-1][j]=best
    
    else:
        F[i][j]=tspf(i,j-1,F,D)+D[j-1][j]

    return F[i][j]

Points=[[0, 1], [11, 5], [4, 2], [2, 1], [1, 3]]
print(tsp(Points))
