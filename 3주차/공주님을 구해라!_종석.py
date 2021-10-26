N, M, T = map(int, input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visit[0][0] = 1
stack =[[0,0]]
stack2 = []
cnt = 0
sword_dir = []
result = []
while stack:
    x, y = stack.pop()

    for i in range(4):
        di = x + dx[i]
        dj = y + dy[i]

        if -1 < di < N and -1 < dj < M and visit[di][dj] == 0 and lst[di][dj] != 1: # 방문 하지 않았고 벽이 아니면
            if lst[di][dj] == 2: # 검이 있다면
                visit[di][dj] = 1
                sword_dir.append([di, dj, cnt+1])

            elif (di, dj) == (N-1, M-1): # 공주님이 있는 위치
                result.append(cnt+1)
                visit[di][dj] = 1

            else:
                visit[di][dj] = 1
                stack2.append([di, dj])

    if not stack and stack2:
        cnt += 1
        stack = stack2[:]
        stack2 = []

# BFS 한번 돌고 나면 4가지 경우가 있다
# 1. 검도 못찾고 공주도 못찾음
# 2. 검만 찾을 수 있는 경우
# 3. 공주만 찾는 경우
# 4. 둘다 찾는 경우

if not result and not sword_dir: # 1. 둘다 못찾음
    print('Fail')
elif not result and sword_dir: # 2. 검만 찾음
    if (N-1 -sword_dir[0][0]) + (M-1 - sword_dir[0][1]) + sword_dir[0][2] <= T:
        print((N-1 -sword_dir[0][0]) + (M-1 - sword_dir[0][1]) + sword_dir[0][2])
    else:
        print('Fail')
elif result and not sword_dir: # 3. 공주만 찾음
    if min(result) <= T:
        print(min(result))
elif result and sword_dir: # 4. 둘다 찾음  --- > 둘다 찾은 경우엔 어떤게 최소값인지 확인해야됨
    result.append((N-1 - sword_dir[0][0]) + (M-1 - sword_dir[0][1]) + sword_dir[0][2])
    if min(result) <= T:
        print(min(result))
    else:
        print('Fail')












