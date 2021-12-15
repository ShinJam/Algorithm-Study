import sys


N = int(sys.stdin.readline())
workTime = [0] * (N + 1)
precede = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    temp = list(map(int, sys.stdin.readline().split()))
    workTime[i] = temp[0]
    precede[i] = (sorted(temp[2:]))

dp = [0] * (N + 1)
for i in range(1, N + 1):
    dp[i] = workTime[i]
    for w in precede[i]:
        dp[i] = max(dp[i], dp[w] + workTime[i])

print(max(dp))
