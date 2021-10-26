# 아직 푸는중....

N, M = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(M)]
parent = [0] * (N+1)
rank = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])

    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
print(parent)
for x, y in lst:

    union_parent(parent, x, y)

print(parent)