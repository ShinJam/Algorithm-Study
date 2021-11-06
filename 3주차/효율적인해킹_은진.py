from collections import deque
import sys
def input(): return sys.stdin.readline().split()

n, m = map(int, input())
graph = [[] for _ in range(n+1)]
res = [0]

for _ in range(m):
  a, b = map(int, input())
  graph[b].append(a)


def bfs(start):
  queue = deque([start])
  visited[start] = 1

  while queue:
    x = queue.popleft()

    for node in graph[x]:
      if visited[node] == 0:
        visited[node] = 1
        queue.append(node)

  return sum(visited)


for i in range(1, n+1):
  visited = [0]*(n+1)
  res.append(bfs(i))

max_res = max(res)
for i in range(1, n+1):
  if res[i] == max_res:
    print(i, end=' ')
