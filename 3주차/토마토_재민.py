from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())
board = []
queue = []
for c in range(N):
    board.append(list(map(int, input().split())))
    for r in range(M):
        if board[c][r] == 1:
            queue.append((r, c, 0))
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
cnt = 0
def bfs():
    global cnt, queue
    queue = deque(queue)
    while queue:
        x, y, t = queue.popleft()
        cnt = t
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            
            if not (0<=nx<M and 0<=ny<N):
                continue
            if board[ny][nx] != 0:
                continue
                
            board[ny][nx] = 1
            queue.append((nx, ny, t+1))
bfs()
for n in range(N):
    for m in range(M):
        if board[n][m] == 0:
            cnt = -1
            break
print(cnt)
