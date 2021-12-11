from collections import defaultdict


def check(nodes) -> bool:
    if len(nodes) != sum(nodes.values()) +1:
        return False
    return True


def make_nodes():
    nodes = dict()  # key: child, value: parent cnt
    tt = []
    while True:
        input_line = input().split()
        for i in range(0, len(input_line)-1, 2):
            u, v = input_line[i:i+2]
            if (u, v) == ('0','0'):
                return nodes
            elif (u, v) == ('-1','-1'):
                return False
            
            if u not in nodes:
                nodes[u] = 0
            if v in nodes:
                nodes[v] += 1
            else:
                nodes[v] = 1
case = 1
while True:
    nodes = make_nodes()
    if nodes == False:
        break
    if check(nodes):
        print(f"Case {case} is a tree.")
    else:
        print(f"Case {case} is not a tree.")
    case+= 1
