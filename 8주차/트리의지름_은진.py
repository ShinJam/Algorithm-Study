import sys
import heapq
sys.setrecursionlimit(10 ** 6)
si = sys.stdin.readline

# 지름의 최댓값
# 탐색한 반지름 중 가장 긴 두 반지름을 선택한 합의 최댓값

def dfs(v):
  global diameter

  if len(tree[v]) == 0:  # leaf node
    return 0

  if len(tree[v]) == 1:
    c, w = tree[v][0]
    r = dfs(c) + w

    if r > diameter:
      diameter = r
    return r

  radius = []
  if len(tree[v]) >= 2:
    for c, w in tree[v]:  # 인접리스트 탐색
      r = dfs(c) + w
      heapq.heappush(radius, -r)

    r_1st = -heapq.heappop(radius)
    r_2nd = -heapq.heappop(radius)

    if r_1st + r_2nd > diameter:
      diameter = r_1st + r_2nd

  return r_1st


n = int(si())
tree = [[] for _ in range(n + 1)]  # 인접리스트

for _ in range(n - 1):
  p, c, w = map(int, si().split())
  tree[p].append((c, w))

diameter = 0
dfs(1)
print(diameter)
