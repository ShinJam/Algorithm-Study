M, N = map(int,input().split()) # M은 가로 N 은 세로
lst = [list(map(int,input().split())) for _ in range(N)]
visit_lst = [[0] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
stack = []
stack2 = []

for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            stack.append([i,j])
            visit_lst[i][j] = 1

cnt = 0
while stack:
    x, y = stack.pop()

    for i in range(4):
        di = x + dx[i]
        dj = y + dy[i]

        if -1 < di < N and -1 < dj < M and visit_lst[di][dj] == 0 and lst[di][dj] == 0:
            visit_lst[di][dj] = 1
            lst[di][dj] = 1
            stack2.append([di, dj])

    if not stack and stack2:
        stack = stack2[:]
        stack2 = []
        cnt += 1

flag = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            flag = 1

if flag == 1:
    print(-1)
else:
    print(cnt)
