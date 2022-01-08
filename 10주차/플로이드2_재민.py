from math import inf
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

def find_path(i, j):
    if prev[i][j] == 0:
        return []
    
    k = prev[i][j]
    return find_path(i, k) + [k] + find_path(k, j)

cost=[[inf for _ in range(N+1)] for _ in range(N+1)]
 
for _ in range(M):
    a,b,c=map(int,input().split())
    cost[a][b]=min(c,cost[a][b])

prev=[[0 for _ in range(N+1)] for _ in range(N+1)]

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i==j:
                cost[i][j]=0
            elif cost[i][j] > cost[i][k]+cost[k][j]:
                cost[i][j] = cost[i][k]+cost[k][j]
                prev[i][j] = k

for i in range(1,N+1):
    for j in range(1,N+1):
        if cost[i][j]==inf:
            print(0,end=" ")
        else:
            print(cost[i][j],end=" ")
    print()
    
for i in range(1, N+1):
    for j in range(1, N+1):
        if i==j or prev[i][j] ==inf:
            print(0)
            continue
        path = [i] + find_path(i, j) + [j]
        print(len(path), end=' ')
        print(*path)
