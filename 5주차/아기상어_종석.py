import sys
sys.stdin = open('아기상어_종석.txt')

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
shark = []
visit_lst = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if lst[i][j] == 9:
            shark.append([i, j])
            lst[i][j] = 0
result = 0
shark2 = []
shark_info = [2, 0]

while True:
    visit_lst = [[0] * N for _ in range(N)]
    fish_lst = []
    cnt = 0
    while shark:
        x, y = shark.pop()
        visit_lst[x][y] = 1

        for w in range(4):
            di = x + dx[w]
            dj = y + dy[w]

            if -1 < di < N and -1 < dj < N and visit_lst[di][dj] == 0 and lst[di][dj] <= shark_info[0]:
                if lst[di][dj] != 0 and lst[di][dj] < shark_info[0]:
                    fish_lst.append([cnt+1, di, dj, lst[di][dj]])
                visit_lst[di][dj] = 1
                shark2.append([di, dj])

        if not shark and shark2:
            shark = shark2[:]
            shark2 = []
            cnt += 1
    if fish_lst:
        fish_lst.sort(key=lambda x: (x[0], x[1], x[2]))
        shark = [[fish_lst[0][1], fish_lst[0][2]]]
        lst[fish_lst[0][1]][fish_lst[0][2]] = 0
        shark_info[1] += 1
        result += fish_lst[0][0]
        if shark_info[0] == shark_info[1]:
            shark_info[0], shark_info[1] = shark_info[0]+1, 0
    else:
        print(result)
        break
