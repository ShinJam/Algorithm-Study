import sys
si = sys.stdin.readline

t = int(si())
for _ in range(t):
  n = int(si())

  tree = [-1 for _ in range(n + 1)]
  for _ in range(n-1):
    p, c = map(int, si().split())
    tree[c] = p  # 역방향 tree

  node1, node2 = map(int, si().split())
  parents = set([])

  while True:
    parents.add(node1)

    if tree[node1] == -1:
      break
    node1 = tree[node1]

  while True:
    if node2 in parents:
      print(node2)
      break

    if tree[node2] == -1:
      break
    node2 = tree[node2]
