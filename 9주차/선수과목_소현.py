import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

indegree = [0] * (n+1)
ans = [0] * (n+1)

#방향 그래프의 간선 정보를 입력받음
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)  # 정점A에서 B로 이동
    indegree[b] += 1  


def TopologicalSort():
    queue = deque()

    for i in range(1, n+1):     
        if indegree[i] == 0:
            queue.append(i)
            ans[i] = 1      

    while queue:
        now = queue.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            ans[i] = ans[now] + 1

            if indegree[i] == 0:
                queue.append(i)
                
TopologicalSort()
print(*ans[1:])
