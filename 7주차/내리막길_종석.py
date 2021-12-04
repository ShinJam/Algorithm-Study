M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
lst2 = [[0] * N for _ in range(M)]
lst2[0][0] = 1
start= [[0, 0]]
check = {}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
start2 = []
result = 0
while start:

    x, y = start.pop()
    cnt = lst[x][y]

    for w in range(4):
        di = x + dx[w]
        dj = y + dy[w]

        if -1 < di < M and -1 < dj < N:

            if cnt > lst[di][dj]:

                if (di, dj) not in check:
                    check[(di, dj)] = 1
                    start.append([di, dj])
                else:
                    result +=1


print(check)
print(result)

if (M-1, N-1) not in check:
    print(0)
else:
    print(check[(M-1, N-1)] + result)
