import sys

N = int(sys.stdin.readline().rstrip())
duration = []
cost = []

for _ in range(N):
    d, c = map(int, sys.stdin.readline().split())
    duration.append(d)
    cost.append(c)

dp = [0] * (N + 1)
max_val = 0
for i in range(N - 1, -1, -1):
    if i + duration[i] <= N:
        dp[i] += cost[i] + dp[i + duration[i]]
    if dp[i] >= max_val:
        max_val = dp[i]
    else:
        dp[i] = max_val
print(max_val)
