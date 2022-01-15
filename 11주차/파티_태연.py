import sys
from collections import defaultdict
import heapq


N, M, X = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
graph_rev = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])
    graph_rev[v].append([u, w])


def dijkstra(start, graph):
    distances = [float('inf')] * (N + 1)
    distances[start] = 0

    pq = []
    heapq.heappush(pq, [distances[start], start])
    while pq:
        weight, node = heapq.heappop(pq)

        if distances[node] < weight:
            continue
        for adjacent, next_weight in graph[node]:
            if distances[node] + next_weight < distances[adjacent]:
                distances[adjacent] = distances[node] + next_weight
                heapq.heappush(pq, [distances[adjacent], adjacent])

    return distances


distancesFromX = dijkstra(X, graph)
distancesToX = dijkstra(X, graph_rev)

max_ = -1
for i in range(1, N + 1):
    max_ = max(max_, distancesToX[i] + distancesFromX[i])

print(max_)
