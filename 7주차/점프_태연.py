import sys

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = 0
# que = [[0, 0]]
# while que:
#     x, y = que.pop()
#
#     if (x, y) == (N - 1, N - 1):
#         answer += 1
#         continue
#
#     if graph[x][y] == 0:
#         continue
#
#     value = graph[x][y]
#     if x + value < N:
#         que.append([x + value, y])
#
#     if y + value < N:
#         que.append([x, y + value])
#

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            print(dp[i][j])
            exit(0)
        value = graph[i][j]
        if i + value < N:
            dp[i + value][j] += dp[i][j]
        if j + value < N:
            dp[i][j + value] += dp[i][j]
