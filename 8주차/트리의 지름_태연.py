import sys
from collections import defaultdict
sys.setrecursionlimit(100000)


def bfs(now, weight):
    visited[now] = True
    if graph.get(now):
        temp = False
        for next_, cost in graph[now]:
            if not visited.get(next_):
                temp = True
                bfs(next_, weight + cost)
        if not temp:
            startNode[now] = weight
    else:
        startNode[now] = weight


N = int(sys.stdin.readline())
graph = defaultdict(list)
while True:
    try:
        parent, child, cost = map(int, sys.stdin.readline().split())
        graph[parent].append([child, cost])
        graph[child].append([parent, cost])
    except Exception:
        break

startNode = dict()
visited = dict()
bfs(1, 0)

temp = sorted(startNode.items(), key=lambda x: [-x[1], x[0]])
start = temp[0][0]
visited.clear()
startNode.clear()
bfs(start, 0)
startNode = sorted(startNode.items(), key=lambda x: [-x[1], x[0]])

print(startNode[0][1])
