from heapq import heappush, heappop
from collections import defaultdict
import sys

input = sys.stdin.readline

def dijk(graph, start):
    dist = defaultdict(lambda:float("inf"))
    dist[start] = 0
    queue = [(0, start)]
    while queue:
        d, v = heappop(queue)
        for l, u in graph[v]:
            alt = dist[v] + l 
            if alt < dist[u]:
                dist[u] = alt
                heappush(queue, (dist[u], u))
    return dist

graph = defaultdict(list)
graph_r = defaultdict(list)

N, M, X = map(int, input().split())
for _ in range(M):
    a, b, d = map(int, input().split())
    graph[a-1].append((d, b-1))
    graph_r[b-1].append((d, a-1))

ans = [0] * N
dist = dijk(graph, X-1)
for k, v in dist.items():
    ans[k] += v
dist = dijk(graph_r, X-1)
for k, v in dist.items():
    ans[k] += v
print(max(ans))
