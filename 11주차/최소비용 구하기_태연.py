import sys
import heapq


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
INF = float('inf')

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])
start, end = map(int, sys.stdin.readline().split())

distances = [INF] * (N + 1)
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

print(distances[end])
