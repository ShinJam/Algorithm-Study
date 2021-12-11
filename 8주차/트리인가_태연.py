import sys
from collections import defaultdict


def check(uNode, vNode, Node):
    try:
        if max(list(vNode.values())) > 1:
            return False
    except Exception:
        return True

    u = set(uNode.keys())
    v = set(vNode.keys())
    temp = u - v
    if len(temp) != 1:
        return False

    return True


uNode = defaultdict(int)
vNode = defaultdict(int)
Node = defaultdict(list)
number = 0
token = False
while True:
    if token:
        break
    case = sys.stdin.readline().rstrip().split("  ")
    for c in case:
        if c == "0 0":
            k = check(uNode, vNode, Node)
            number += 1
            if k:
                print("Case {} is a tree.".format(number))
            else:
                print("Case {} is not a tree.".format(number))

            uNode = defaultdict(int)
            vNode = defaultdict(int)
            Node = defaultdict(list)

        else:
            try:
                u, v = map(int, c.split())
                if u < 0 and v < 0:
                    token = True
                    break
                else:
                    uNode[u] += 1
                    vNode[v] += 1
                    Node[u].append(v)
            except Exception:
                continue
