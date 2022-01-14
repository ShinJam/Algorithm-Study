import sys
si = sys.stdin.readline
INF = 10_000_000  # sys.maxsize

n = int(si())
m = int(si())
graph = [[INF]*(n+1) for _ in range(n+1)]
mid = [[0]*(n+1) for _ in range(n+1)]

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
      if graph[i][j] > graph[i][k] + graph[k][j]:
        graph[i][j] = graph[i][k] + graph[k][j]
        mid[i][j] = k


# 최소 비용 출력
for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] == INF:
      graph[i][j] = 0
    print(graph[i][j], end=" ")
  print()


# 경유지 확인 (중위 순회)
def get_mid(s, e):
  if mid[s][e] == 0:
    return

  k = mid[s][e]
  get_mid(s, k)
  path.append(k)
  get_mid(k, e)


# 최소 비용 경로 출력
for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] == 0:
      print(0)
    elif mid[i][j] == 0:
      print(2, i, j)
    else:
      path = []
      get_mid(i, j)
      print(len(path) + 2, i, *path, j)
