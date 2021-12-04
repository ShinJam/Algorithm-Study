import sys
sys.setrecursionlimit(10**9)       #런타임에러

m, n = map(int, sys.stdin.readline().split())
height = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]   
#dp[m-1][n-1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):

    if x == m-1 and y == n-1:
        return 1

    if dp[x][y] == -1:  
        dp[x][y] = 0    

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if height[x][y] > height[nx][ny]:
                    dp[x][y] += dfs(nx, ny)
    return dp[x][y]


print(dfs(0,0))

