N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
lst2 = [[0] * N for _ in range(N)]
lst2[0][0] = 1
for i in range(N):
    for j in range(N):

        di = i + lst[i][j]
        dj = j + lst[i][j]

        if lst[i][j] == 0:
            continue

        if -1 < di < N:
            lst2[di][j] += lst2[i][j]
        if -1 < dj < N:
            lst2[i][dj] += lst2[i][j]

print(lst2[-1][-1])







