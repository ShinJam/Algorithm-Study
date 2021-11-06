import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)  

result = []
max_value = -1

def bfs(start):
    queue = deque([start])
    visited = [False] * (n + 1)  
    visited[start] = True
    count = 1

    while queue:
        v = queue.popleft()  
        for e in graph[v]:  
            if not visited[e]: 
                queue.append(e)  
                visited[e] = True  
                count += 1  

    return count  


for i in range(n):  
    count = bfs(i)  
    if count > max_value:  
        max_value = count  
        result = [i]  
    elif count == max_value:  
        result.append(i)  

for r in result:
    print(r, end=" ")
