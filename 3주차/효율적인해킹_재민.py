# pypy
import sys
input = sys.stdin.readline

from collections import defaultdict, deque
N, M = map(int, input().split())
nodes = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    nodes[b].append(a)
    
def bfs(node):
    visited = [0]*(N+1)
    visited[node] = 1
    cnt = 1 
    queue = deque([node])
    while queue:
        u = queue.popleft()
        for i in nodes[u]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
                cnt += 1
    return cnt

_max = 0
answer = []
for i in range(1, N+1):
    result = bfs(i)
    if result > _max:
        _max = result
        answer = [i]
    elif result == _max:
        answer.append(i)
print(*answer)
