from collections import deque
import sys

input = sys.stdin.readline

def best_one(x, y, t):
    global size, cnt, board
    queue = deque([(t, y, x)])
    visit = {(x, y)}
    
    ret = []
    
    while queue:
        t, y, x= queue.popleft()
        if board[y][x] and board[y][x] < size:
            ret.append((t, y, x))
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if not (0<=nx<N and 0<=ny<N):
                continue
            if board[ny][nx] > size:
                continue
            if (nx, ny) in visit:
                continue
            queue.append((t+1, ny, nx))
            visit.add((nx, ny))
    ret.sort()
    if ret:
        t, y, x = ret[0]
        board[y][x] = 0
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0
        return x, y, t
    return None



dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
cnt = 0
size = 0


N = int(input())
board = []
x, y, size = 0, 0, 2
for c in range(N):
    row = list(map(int, input().split()))
    for r, val in enumerate(row):
        if val == 9:
            x, y = r, c
            row[r] = 0
    board.append(row)
    
    
    
def solve(x, y):
    pos = (x, y, 0)
    time = 0
    while True:
        pos = best_one(*pos)
        if not pos:
            return time
        time = pos[2]
        
print(solve(x, y))
