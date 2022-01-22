import sys
input = sys.stdin.readline

n, m = map(int, input().split())

road = []
for _ in range(m):
    a, b, c = map(int, input().split())
    road.append((c, a, b))
road.sort(reverse=True)
#=> 최대한 무거운 물건을 옮기기 위해, 최소가 아닌 최대 스패닝 트리를 구하기 위해 내림차순 정렬해준다

fac1, fac2 = map(int, input().split())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX < rootY:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY


for i in road:
    c, x, y = i[0], i[1], i[2]
    union(parent, x, y)
    if find(parent, fac1) == find(parent, fac2):
        break
print(c)
