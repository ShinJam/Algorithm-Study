from collections import deque
from math import inf

import sys

input =sys.stdin.readline
      
N, M, T = map(int, input().split())
BOARD = []
sword = tuple()
for j in range(N):
    row = list(map(int, input().split()))
    BOARD.append(row)
    for i in range(M):
        if row[i] == 2:
            sword = (i, j)    

            
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
queue = deque([(0,0,1)]) # x, y, 시간
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
sword_cnt = inf
ret = inf
while queue:
    x, y, t = queue.popleft()

    if (x, y) == sword:
        sword_cnt = min(sword_cnt, t-1)
    if (x, y) == (M-1, N-1):
        ret = min(ret, t-1)

    for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        if not(0<=nx<M and 0<=ny<N):
            continue
        if visited[ny][nx]:
            continue
        if BOARD[ny][nx]==1:
            continue
        queue.append((nx, ny, t+1))
        visited[ny][nx] = 1
            
sword_cnt += ((N-1-sword[1])+(M-1-sword[0]))

ret = ret if ret < sword_cnt else sword_cnt

if ret <= T:
    print(ret)
else:
    print("Fail")
