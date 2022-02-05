import sys

input =sys.stdin.readline
N = int(input())

max_dp = [0] * 3
min_dp = [0] * 3


for _ in range(N):
    a, b, c = map(int, input().split())
    
    tmp_a, tmp_c = max_dp[0], max_dp[2]
    max_dp[0] = max(max_dp[0], max_dp[1]) + a
    max_dp[2] = max(max_dp[1], max_dp[2]) + c
    max_dp[1] = max(tmp_a, max_dp[1], tmp_c) + b
    
    tmp_a, tmp_c = min_dp[0], min_dp[2]
    min_dp[0] = min(min_dp[0], min_dp[1]) + a
    min_dp[2] = min(min_dp[1], min_dp[2]) + c
    min_dp[1] = min(tmp_a, min_dp[1], tmp_c) + b
print(max(max_dp), min(min_dp))
