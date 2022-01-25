import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
priority = []
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(priority, [-c, a, b])
start, end = map(int, sys.stdin.readline().split())

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
    p[v] = p1

while priority:
    cost, x, y = heapq.heappop(priority)
    union(x, y)
    if find(start) == find(end):
        break

print(-cost)
