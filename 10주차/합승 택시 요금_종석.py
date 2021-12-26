def solution(n, s, a, b, fares):
    lst = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        lst[i][i] = 0

    for x, y, weight in fares:
        lst[x - 1][y - 1] = lst[y - 1][x - 1] = weight

    for k in range(n):
        for x in range(n):
            for y in range(n):
                if lst[x][y] > lst[x][k] + lst[k][y]:
                    lst[x][y] = lst[x][k] + lst[k][y]

                # lst[x][y] = min(lst[x][y], lst[x][k] + lst[k][y])
                # 위에 if 문이랑 아래 min으로 값 찾는 방법이 시간이 2배정도 차이남

    cnt = float('inf')
    for i in range(n):
        check = lst[s - 1][i] + lst[i][a - 1] + lst[i][b - 1]
        if check <= cnt:
            cnt = check
    # print(cnt)
    return cnt


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
solution(n, s, a, b, fares)
