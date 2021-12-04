#dp풀이

import sys

n = int(sys.stdin.readline().rstrip())
jump_box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]    
dp[0][0] = 1    


for i in range(n):
    for j in range(n):
        now = jump_box[i][j]

        nx = i + now    #아래쪽
        ny = j + now    #오른쪽

        if now > 0:
            if nx < n:
                dp[nx][j] += dp[i][j]   #아래쪽으로 가기
            if ny < n:
                dp[i][ny] += dp[i][j]   #오른쪽으로 가기

                
print(dp[-1][-1])
