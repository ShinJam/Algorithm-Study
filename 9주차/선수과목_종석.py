N, M = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(M)]
lst.sort()
visit = [0] * N
L = len(visit)
stack = []
node = {}
node2 = {}
new_visit = [0] * N
for x, y in lst:
    if y not in node:
        node[y] = [x]
    else:
        node[y].append(x)

    if x not in node2:
        node2[x] = [y]
    else:
        node2[x].append(y)

    if visit[x - 1] == 0:
        visit[x - 1] = 1
        visit[y - 1] = 1
        new_visit[x - 1] = 1
        stack.append(x)
    elif visit[x - 1] == 1:
        visit[y - 1] = 1
stack2 = []
cnt = 1
visit = [0] * N

while stack:
    target = stack.pop()
    if visit[target - 1] == 0:
        visit[target - 1] = cnt
        check = []
        if target in node2:
            for i in node2[target]:
                check.append(i)

            for j in check:
                if j in node:
                    for k in node[j]:
                        if visit[k - 1] == 0:
                            break
                    else:
                        stack2.append(j)

        if not stack and stack2:
            stack = stack2[:]
            stack2 = []
            cnt += 1

for w in visit:
    if w == 0:
        print(1, end=' ')
    else:
        print(w, end=' ')
