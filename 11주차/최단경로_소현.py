import heapq, sys

input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
k = int(input())    #start; 시작정점의 번호

distance = [INF] * (v+1)

graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(k):
    h = []
    heapq.heappush(h, (0, k))   #힙큐에 출발점을 넣어줌(거리, 출발지점)
    distance[k] = 0

    while h:
        dist, now = heapq.heappop(h)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))
dijkstra(k)


for i in range(1, v+1):
    if distance[i] == INF:
        print('int')
    else:
        print(distance[i])
