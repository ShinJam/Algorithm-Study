# 시간 초과 ... 눈물

N, M = map(int,input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
problem = {i: {} for i in range(1, N+1)}
result = []
for x, y in lst:

    problem[y].update({x: x})

check = []
stack = []
for key, value in problem.items():
    if len(value) == 0:
        check.append(key)
        stack.append(key)
for i in check:
    del problem[i]

stack.sort(reverse=True)

while stack:

    target = stack.pop()
    result.append(target)
    check = []
    for key, value in problem.items():

        if target in value:
            check.append([key, target])

    for key, target in check:
        del problem[key][target]

    check2 = []
    for key, value in problem.items():
        if len(value) == 0:
            check2.append(key)
            stack.append(key)

    for i in check2:
        del problem[i]

    stack.sort(reverse=True)

print(*result)


