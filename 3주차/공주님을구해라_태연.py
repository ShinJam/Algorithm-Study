import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().split())
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]
que = deque()
que.append([0, 0, 0])
visited[0][0] = True
answer = float('inf')

while que:
    x, y, count = que.popleft()

    if count > T:
        break
    if x == N - 1 and y == M - 1:
        answer = min(answer, count)
        break

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            if board[nx][ny] == 0:
                que.append([nx, ny, count + 1])
            elif board[nx][ny] == 2:
                answer = min(answer, count + 1 + N - 1 - nx + M - 1 - ny)

if answer > T:
    print('Fail')
else:
    print(answer)

