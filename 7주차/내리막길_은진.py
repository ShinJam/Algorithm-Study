import sys
sys.setrecursionlimit(10 ** 6)
si = sys.stdin.readline


def dp(x, y):
  if visited[x][y] > -1:  # 메모이제이션
    return visited[x][y]
  else:
    visited[x][y] = 0  # 방문

  for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
    nx, ny = x + dx, y + dy
    if (0 <= nx < n) and (0 <= ny < m):
      if graph[nx][ny] < graph[x][y]:  # 내리막
        visited[x][y] += dp(nx, ny)

  return visited[x][y]


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]

visited = [[-1] * m for _ in range(n)]
visited[n-1][m-1] = 1

print(dp(0, 0))
