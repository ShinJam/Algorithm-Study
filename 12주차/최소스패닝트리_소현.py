#크루스칼 구현
import sys
input = sys.stdin.readline

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 크루스칼 알고리즘은 간선 비용순으로 오름차순 정렬하기 때문에 이를 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))
edges.sort()

# 특정 원소가 속한 집합을 찾기
def find(parent, x):
    #루트 노드의 부모 노드 번호는 자기 자신이다
    if parent[x] == x:
        return x
    # 각 노드의 부모 노드를 찾아 올라간다
    # find하면서 만나는 모든 값의 부모 노드를 root로 만든다
    parent[x] = find(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기 (=간선 연결한다고 생각!)
def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX < rootY:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY

# 최소 비용의 간선 사이에서 find를 적용하여
# 사이클 되지 않은 두 정점이 존재하면 union을 적용한다.

result = 0
# 사이클 확인 후 연결
for edge in edges:
    cost, x, y = edge
    # 사이클이 발생하지 않는 경우에만 간선을 선택한다 = 집합에 포함한다(=연결한다)
    if find(parent, x) != find(parent, y):
        union(parent, x, y)
        result += cost

print(result)
