from collections import defaultdict
from heapq import *

N, M = map(int,input().split())


graph = defaultdict(list)
indegree_cnt = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    indegree_cnt[b-1] += 1
    graph[a-1].append(b-1)

queue = []
for v in range(N):
    if indegree_cnt[v] == 0:
        heappush(queue, v)

while queue:
    v = heappop(queue)
    print(v+1, end=" ")
    for k in graph[v]:
        indegree_cnt[k] -= 1
        if indegree_cnt[k] == 0:
            heappush(queue, k)
