import sys
from collections import defaultdict
import heapq

N, M = map(int, sys.stdin.readline().split())
minHeap = []
p = defaultdict(list)
p_count = defaultdict(int)
dp = [1] * (N + 1)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    p[A].append(B)
    p_count[B] += 1

result = []
for i in range(1, N + 1):
    if not p_count.get(i):
        heapq.heappush(minHeap, i)

while minHeap:
    minNumber = heapq.heappop(minHeap)
    for next_ in p[minNumber]:
        p_count[next_] -= 1
        dp[next_] = max(dp[minNumber] + 1, dp[next_])
        if p_count[next_] == 0:
            heapq.heappush(minHeap, next_)

print(*dp[1:])
