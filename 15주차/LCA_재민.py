from collections import defaultdict

graph = defaultdict(list)


N = int(input())
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    
depth = [-1] * (N+1)
parent = [0] * (N+1)

def check_depth(n, d):
    depth[n] = d
    
    for v in graph[n]:
        if depth[v] != -1:
            continue
        parent[v] = n
        check_depth(v, d+1)

check_depth(1, 0)

def LCA(a, b):
    while depth[a]!=depth[b]:
        if depth[a] < depth[b]:
            b = parent[b]
        elif depth[a] > depth[b]:
            a = parent[a]
    while a!=b:
        a = parent[a]
        b = parent[b]
    return a
    
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(LCA(a, b))
    
