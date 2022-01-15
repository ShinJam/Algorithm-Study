import sys
import heapq


V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]
INF = float('inf')

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])


visit = [False] * (V + 1)
distances = [INF] * (V + 1)

distances[start] = 0
visit[start] = True

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

for cost in distances[1:]:
    if cost == INF:
        print("INF")
    else:
        print(cost)
