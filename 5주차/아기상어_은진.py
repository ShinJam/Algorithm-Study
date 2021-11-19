import sys
from collections import deque
def input(): return sys.stdin.readline()

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


def bfs(x, y):
  global shark, total_time, fish

  visited = [[0]*n for _ in range(n)]
  visited[x][y] = 0
  queue = deque([[x, y, 0]])
  fish_net = []
  flag = 500

  while queue:
    if queue[0][2] < flag:
      x, y, time = queue.popleft()

      for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy

        if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny]:
          if 0 < graph[nx][ny] < shark:  # 먹을 수 있는 물고기
            fish_net.append([nx, ny])
            flag = time + 1

            visited[nx][ny] = 1
            queue.append([nx, ny, time + 1])

          elif graph[nx][ny] == 0 or graph[nx][ny] == shark:  # 지나갈 수 있음
            visited[nx][ny] = 1
            queue.append([nx, ny, time + 1])

    else:  # 최단 경로 탐색 완료, 물고기 섭취, 출발지 재설정
      fish_net.sort(key=lambda v: (v[0], v[1]))
      x, y = fish_net[0]

      fish += 1
      graph[x][y] = 0
      total_time += flag

      visited = [[0]*n for _ in range(n)]
      visited[x][y] = 1
      queue = deque([[x, y, 0]])
      fish_net = []
      flag = 500

      if fish == shark:
        fish = 0
        shark += 1


shark = 2
total_time = 0
fish = 0

for i in range(n):
  for j in range(n):
    if graph[i][j] == 9:
      graph[i][j] = 0
      bfs(i, j)
      break

print(total_time)
