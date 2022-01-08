from math import inf
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())


cost=[[inf for _ in range(N+1)] for _ in range(N+1)]
 
for _ in range(M):
    a,b,c=map(int,input().split())
    cost[a][b]=min(c,cost[a][b])
 
 
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i==j:
                cost[i][j]=0
            else:
                cost[i][j]=min(cost[i][j],cost[i][k]+cost[k][j])

for i in range(1,N+1):
    for j in range(1,N+1):
        if cost[i][j]==inf:
            print(0,end=" ")
        else:
            print(cost[i][j],end=" ")
    print()
