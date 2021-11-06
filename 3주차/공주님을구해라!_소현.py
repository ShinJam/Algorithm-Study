#실패

import sys
from collections import deque

n, m, t = map(int, sys.stdin.readline().split())

castle = []
for i in range(n):
    castle.append(list(map(int, sys.stdin.readline().split())))
visited = [[0] * n for _ in range(n)]
princess = 987654321

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global princess
    queue = deque([])
    queue.append((0,0))
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()
        if castle[x][y] == 2:
            princess = abs(n-1-x) + abs(m-1-y) + visited[x][y] -1
        if x == n-1 and y == m-1:
            return min(visited[x][y]-1, princess)

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    queue.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1

    return princess

if princess < t:
    print("Fail")
else:
    print(bfs())
