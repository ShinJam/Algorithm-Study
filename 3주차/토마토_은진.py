import sys
from collections import deque
def input(): return sys.stdin.readline().split()

m, n = map(int, input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
  day = 0
  queue = deque([])

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        queue.append([i, j])

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if (0 <= nx < n) and (0 <= ny < m):
        if graph[nx][ny] == 0:
          graph[nx][ny] = graph[x][y] + 1
          queue.append([nx, ny])
          day = graph[x][y]
  
  return day


def haszero():
  for i in range(n):
    if 0 in graph[i]:
      return True
  return False


res = bfs()
print(res if not haszero() else -1)
