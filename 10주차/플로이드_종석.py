n = int(input())
m = int(input())
bus_info = [list(map(int, input().split())) for _ in range(m)]
lst = [[float('inf')] * n for _ in range(n)]

for i in range(n):
    lst[i][i] = 0

for x, y, weight in bus_info:
    lst[x-1][y-1] = min(lst[x-1][y-1], weight)

for k in range(n):
    for x in range(n):
        for y in range(n):
            lst[x-1][y-1] = min(lst[x-1][y-1], lst[x-1][k-1] + lst[k-1][y-1])

for i in range(n):
    for j in range(n):

        if lst[i][j] == float('inf'):
            lst[i][j] = 0


for i in lst:
    print(*i)