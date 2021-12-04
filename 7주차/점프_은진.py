import sys
def input(): return sys.stdin.readline().rstrip()

def dp(x, y):
  if (0 > x) or (x >= n) or (0 > y) or (y >= n):
    return 0

  if visited[x][y] != -1:  # 메모이제이션
    return visited[x][y]

  if (x == n - 1) and (y == n - 1):  # 목적지
    visited[x][y] = 1
    return visited[x][y]

  if graph[x][y] == 0:  # 목적지X and 점프X
    visited[x][y] = 0
    return visited[x][y]

  visited[x][y] = dp(x + graph[x][y], y) + dp(x, y + graph[x][y])
  return visited[x][y]


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]

print(dp(0, 0))
