import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
distances = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    distances[i][i] = 0

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if distances[a - 1][b - 1] > c:
        distances[a - 1][b - 1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            if distances[i][j] > distances[i][k] + distances[k][j]:
                distances[i][j] = distances[i][k] + distances[k][j]

for i in range(N):
    for j in range(N):
        if distances[i][j] == float('inf'):
            distances[i][j] = 0

for i in range(N):
    print(*distances[i])
