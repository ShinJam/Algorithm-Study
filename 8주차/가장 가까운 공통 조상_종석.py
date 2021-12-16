T = int(input())
for i in range(T):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N-1)]
    target = list(map(int,input().split()))
    node = {}
    visit_lst = [0] * (N + 1)

    for x, y in lst:
        node[y] = x

    target1, target2 = [target[0]], [target[1]]
    while target1:
        t = target1.pop()
        visit_lst[t] = 1
        if t in node:
            target1.append(node[t])

    while target2:
        t2 = target2.pop()
        if visit_lst[t2] != 1:
            visit_lst[t2] = 1
            if t2 in node:
                target2.append(node[t2])
        else:
            break
    print(t2)
