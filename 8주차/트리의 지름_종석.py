import copy

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n-1)]

if n == 1:
    print(0)
else:
    node = {}
    for x, y, weight in lst:
        if x not in node:
            node[x] = {y: weight}
        else:
            node[x][y] = weight

        if y not in node:
            node[y] = {x: weight}
        else:
            node[y][x] = weight

    start = [[lst[0][0], 0]]
    start2 = []
    start3 = []
    find_child = []
    visit_lst = [0] * (n + 1)
    visit_lst[1] = 1
    visit_lst[0] = 1
    while start:
        target, weight = start.pop()

        if target in node:
            for key, value in node[target].items():
                if visit_lst[key] == 0:
                    visit_lst[key] = 1
                    start2.append([key, weight+value])
                    start3.append([key, weight + value])
        if not start and start2:
            start = copy.deepcopy(start2)
            start2 = []

        if sum(visit_lst) == n+1:
            find_child = start[:]
            break

    start3.sort(key=lambda x:x[1])
    new_start = [[start3[-1][0] , 0]]
    new_start2 = []
    visit_lst = [0] * (n + 1)
    visit_lst[start3[-1][0]] = 1
    visit_lst[0] = 1
    find_child2 = []
    new_start3 = []

    while new_start:

        target, weight = new_start.pop()

        if target in node:
            for key, value in node[target].items():
                if visit_lst[key] == 0:
                    visit_lst[key] = 1
                    new_start2.append([key, weight+value])
                    new_start3.append([key, weight+value])
        if not new_start and new_start2:
            new_start = copy.deepcopy(new_start2)
            new_start2 = []

        if sum(visit_lst) == n+1:
            find_child2 = start[:]
            break
    new_start3.sort(key=lambda x:x[1])
    print(new_start3[-1][-1])


