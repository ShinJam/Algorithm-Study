# 크루스칼 알고리즘

import sys
import heapq
def input(): return sys.stdin.readline()


def find(x):
  if p[x] < 0:  # 루트노드인 경우
    return x

  p[x] = find(p[x])  # 루트노드 할당
  return p[x]


def union(x, y):
  x = find(x)
  y = find(y)

  if p[x] < p[y]:  # x의 하위노드 개수가 더 많을 때
    p[x] += p[y]
    p[y] = x  # y는 더이상 루트노드가 아님
  else:
    p[y] += p[x]
    p[x] = y


n = int(input())
m = int(input())

p = [-1] * (n + 1)
q = []
for _ in range(m):
  a, b, c = map(int, input().split())
  heapq.heappush(q, (c, a, b))

cost = 0
while q:
  c, a, b = heapq.heappop(q)
  a = find(a)
  b = find(b)
  if a != b:  # 루트 노드가 다르다면 : 서로 다른 집합이라면
    union(a, b)
    cost += c

print(cost)
