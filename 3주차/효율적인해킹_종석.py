N, M = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(M)]
trust = {}

for x, y in lst:

    if y not in trust:
        trust[y] = [x]
    else:
        trust[y].append(x)

max_k = 0
result = []

for i in range(1, N + 1):
    visit = [0] * (N+1)
    stack = [i]
    visit[i] = 1
    stack2 = []
    cnt = 0

    while stack:
        target = stack.pop()

        if target in trust:

            for number in trust[target]:
                if visit[number] != 1:
                    cnt +=1
                    stack2.append(number)
                    visit[number] = 1

        if not stack and stack2:
            stack = stack2[:]
            stack2 = []
    if cnt >= max_k:
        max_k = cnt
    result.append([i, cnt])

result.sort(key=lambda x: (-x[1], x[0]))

for r in result:
    if r[1] == max_k:
        print(r[0], end=' ')
    else:
        break