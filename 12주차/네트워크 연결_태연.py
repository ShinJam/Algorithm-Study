import sys
import heapq

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
priority = []
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(priority, [c, a, b])

p = [0]
for i in range(1, V + 1):
    p.append(i)

def find(u):
    if p[u] != u:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    p1 = find(u)
    p2 = find(v)
    p[p2] = p1

costs = 0
edgeCount = 0
while priority:
    if edgeCount == V - 1:
        break
    cost, x, y = heapq.heappop(priority)
    if find(x) != find(y):
        union(x, y)
        costs += cost
        edgeCount += 1

print(costs)
