import sys
import heapq
from collections import defaultdict
def input(): return sys.stdin.readline()
INF = 1_000 * 100_000


def dijkstra(start):
  h = []
  heapq.heappush(h, (0, start))  # 비용, 출발도시
  table[start] = 0

  while h:
    cost, x = heapq.heappop(h)  # 현재비용, 출발도시
    if cost > table[x]:  # 최단경로를 이미 계산한 경우 = 방문한 적 있는 경우
      continue
    for y, w in graph[x]:
      cost_y = cost + w
      if cost_y < table[y]:
        table[y] = cost_y
        heapq.heappush(h, (cost_y, y))


n = int(input())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
  x, y, w = map(int, input().split())
  graph[x].append((y, w))

table = [INF] * (n+1)  # 최단경로 테이블

start, end = map(int, input().split())
dijkstra(start)
print(table[end])
