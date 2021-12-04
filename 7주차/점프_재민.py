N = int(input())
BOARD = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

def result(n, board, dp):
    for c in range(n):
        for r in range(n):
            if r == n-1 and c == n-1:
                return dp[n-1][n-1]
            jump = board[r][c]
            if c + jump < N:
                dp[r][c + jump] += dp[r][c]
            if r + jump < N:
                dp[r + jump][c] += dp[r][c]

ret = result(N, BOARD, dp)
print(ret)
