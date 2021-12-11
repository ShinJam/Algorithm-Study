from collections import defaultdict
import sys

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline())
    tree = defaultdict(list)
    tree_rev = dict()
    for _ in range(N - 1):
        parent, child = map(int, sys.stdin.readline().split())
        tree[parent].append(child)
        tree_rev[child] = parent

    x, y = map(int, sys.stdin.readline().split())

    cur = 1
    while True:
        if tree_rev.get(cur):
            cur = tree_rev[cur]
        else:
            break
    root = cur

    setX = set()
    setY = set()
    setX.add(x)
    setY.add(y)
    while True:
        if x != root:
            setX.add(tree_rev[x])
            x = tree_rev[x]
        if y != root:
            setY.add(tree_rev[y])
            y = tree_rev[y]

        if x in setY:
            print(x)
            break
        if y in setX:
            print(y)
            break
