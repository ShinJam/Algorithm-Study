

N = int(input())
lst = [list(map(int, input().split( ))) for _ in range(N)]
node = {}
time_check = []
for i in range(len(lst)):
    time_check.append(lst[i][0])

    if lst[i][1] == 0:
        node[i+1] = {}
        continue
    else:
        for j in range(2, 2 + lst[i][1]):

            if i+1 not in node:
                node[i+1] = {lst[i][j]: lst[i][j]}
            else:
                node[i+1].update({lst[i][j]: lst[i][j]})

stack = []
check = []
for key, value in node.items():

    if len(value) == 0:
        stack.append([key, time_check[key - 1]])
        check.append(key)

for c in check:
    del node[c]
stack.sort(key= lambda x: -x[1])
time_cnt = 0
while stack:

    target, T = stack.pop()
    time_cnt += T
    for i in range(len(stack)):
        stack[i][1] -= T

    check = []
    check2 = []

    for key, value in node.items():

        if target in value:
            check.append([key, value[target]])

    for key, key2 in check:
        del node[key][key2]
    for key, value in node.items():

        if len(value) == 0:
            stack.append([key, time_check[key-1]])

    for x, y in stack:
        if x in node:
            del node[x]

    stack.sort(key=lambda x: -x[1])

print(time_cnt)