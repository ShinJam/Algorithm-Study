import sys

n = int(sys.stdin.readline().rstrip())

time = []
cost = []
dp = []

for i in range(n):
    Ti, Pi = map(int, sys.stdin.readline().split())
    time.append(Ti)
    cost.append(Pi)
    dp.append(Pi)
dp.append(0)

for i in range(n-1, -1, -1):
    if time[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], cost[i] + dp[i + time[i]])
print(dp[0])
