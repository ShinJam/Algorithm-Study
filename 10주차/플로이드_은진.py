import sys
si = sys.stdin.readline
INF = 10_000_000

n = int(si())
m = int(si())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
  a, b, c = map(int, si().split())
  graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
  graph[k][k] = 0
  for i in range(1, n+1):
    if i == k:
      continue
    for j in range(1, n+1):
      if j == k:
        continue
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] == INF:
      print(0, end=" ")
    else:
      print(graph[i][j], end=" ")
  print()
