import sys
import heapq
def input(): return sys.stdin.readline()
INF = 300_001 * 10

n, e = map(int, input().split())  # 정점, 간선
k = int(input())

distance = [INF for _ in range(n + 1)]  # 최대 가중치 10
graph = [[] for _ in range(n + 1)]

for _ in range(e):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))  # idx: 출발노드, (v, w): 도착노드, 가중치


def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))  # tuple: 비용 0, 시작노드
  distance[start] = 0  # 시작노드의 비용 0

  while q:
    cost, now = heapq.heappop(q)  # 방문노드
    if distance[now] < cost:  # 이미 방문한 경우 (이미 최단경로를 계산한 경우) 무시
      continue
    for to, weight in graph[now]:  # 도착노드, 가중치
      ncost = cost + weight  # 도착노드까지의 비용
      if ncost < distance[to]:  # 도착노드까지의 비용이 최단거리일 경우
        distance[to] = ncost  # 최단경로 테이블 갱신
        heapq.heappush(q, (ncost, to))  # 우선순위 큐에 도착노드와 비용 푸시


dijkstra(k)

print(distance)
for i in range(1, n + 1):
  if distance[i] == INF:
    print('INF')
  else:
    print(distance[i])
