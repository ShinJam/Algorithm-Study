import sys
from collections import defaultdict

N, M, X = map(int, sys.stdin.readline().split())
graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u][v] = w

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

max_ = -1
for i in range(1, N + 1):
    max_ = max(max_, graph[i][X] + graph[X][i])
print(max_)
