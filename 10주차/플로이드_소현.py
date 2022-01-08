import sys

inf = sys.maxsize

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

dist = [[inf] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)


for k in range(n):  # 거치는 점
    for i in range(n):  # 시작점
        for j in range(n):  # 끝점
            if i == j:
                dist[i][j] = 0
            else:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(n):
    for j in range(n):
        if dist[i][j] == int:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
