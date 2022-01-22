# 크루스칼 알고리즘

import sys
def input(): return sys.stdin.readline().split()


def find(x):
  if p[x] < 0:  # x가 루트노드
    return x

  p[x] = find(p[x])
  return p[x]


def union(x, y):
  # x = find(x)
  # y = find(y)

  # if x == y:  # x와 y가 이미 연결된 상태
  #   return

  if p[x] > p[y]:  # y의 집합의 개수가 더 많음 (-집합의 개수)
    p[y] += p[x]  # x의 집합을 y의 집합으로 merge
    p[x] = y  # x는 루트노드가 아님, p[x]는 음수가 아님, x의 루트노드 갱신
  else:
    p[x] += p[y]
    p[y] = x


v, e = map(int, input())
p = [-1 for _ in range(v+1)]

graph = [list(map(int, input())) for _ in range(e)]
graph.sort(key=lambda x: (x[2], x[0], x[1]))
weight = 0

for a, b, c in graph:
  a = find(a)
  b = find(b)
  if a != b:  # a와 b가 연결되지 않은 상태
    weight += c
    union(a, b)

print(weight)
