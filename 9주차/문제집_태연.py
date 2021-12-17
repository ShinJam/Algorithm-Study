import sys
import heapq
from collections import defaultdict


N, M = map(int, sys.stdin.readline().split())
minHeap = []
p = defaultdict(list)
p_count = defaultdict(int)

for _ in range(M):
    easy, hard = map(int, sys.stdin.readline().split())
    p[easy].append(hard)
    p_count[hard] += 1

result = []
for i in range(1, N + 1):
    if not p_count.get(i):
        heapq.heappush(minHeap, i)

while minHeap:
    minNumber = heapq.heappop(minHeap)
    result.append(minNumber)

    for next_ in p[minNumber]:
        p_count[next_] -= 1
        if p_count[next_] == 0:
            heapq.heappush(minHeap, next_)

print(*result)
