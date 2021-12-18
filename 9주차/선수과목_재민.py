import sys
from collections import defaultdict,deque

input = sys.stdin.readline

N, M = map(int, input().split())
in_degree_cnt = [0] * N
dp = [1] * N

graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    in_degree_cnt[b-1] += 1

queue = deque()
for i in range(N):
    if in_degree_cnt[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    for i in graph[node]:
        in_degree_cnt[i] -= 1
        dp[i] = max(dp[node] + 1, dp[i])
        if in_degree_cnt[i] == 0:
            queue.append(i)

print(*dp)
