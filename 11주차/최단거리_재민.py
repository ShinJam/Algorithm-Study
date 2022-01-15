from heapq import heappush, heappop
from collections import defaultdict
from math import inf
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

V, E = map(int, input().split()) 
K = int(input())
for _ in range(E): 
    a, b, d = map(int, input().split())
    graph[a-1].append((d, b-1))

ans = [inf] * V     
dist = dijk(graph, K-1)
for k, v in dist.items():
    ans[k] = v
for r in ans:
    print("INF" if r==inf else r)
