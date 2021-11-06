from collections import deque
import sys
def input(): return sys.stdin.readline().split()

n, m, c = map(int, input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque([[x, y]])
  visited[x][y] = 1

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < n) and (0 <= ny < m) and visited[nx][ny] == 0:
        visited[nx][ny] = visited[x][y] + 1

        if graph[nx][ny] == 0:
          queue.append([nx, ny])


for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      kx, ky = i, j


bfs(0, 0)
res = 10000
flag = False

if visited[n-1][m-1]:
  res = min(res, visited[n-1][m-1] - 1)
  flag = True

if visited[kx][ky]:
  res = min(res, visited[kx][ky] - 1 + (n + m - 2) - (kx + ky))
  flag = True

print(res if flag and res <= c else "Fail")
