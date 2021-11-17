
# 실패 .............. 하는중. ..

import sys
sys.stdin = open('나무 재테크_종석.txt')

import copy
from collections import deque

N, M, K = map(int,input().split())
lst = [[5] * N for _ in range(N)]
winter_info = [list(map(int,input().split())) for _ in range(N)]
tree = [list(map(int,input().split())) for _ in range(M)]
tree_info = {}
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
for x, y, age in tree:
    if (x-1, y-1) not in tree_info:
        tree_info[(x-1, y-1)] = deque()
        tree_info[(x - 1, y - 1)].append(age)
    else:
        tree_info[(x-1, y-1)].append(age)

cnt = 0
while True:
    # 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
    # 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다.
    # 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
    spring_tree = {}
    spring_dead_tree = {}
    summer_tree = {}
    fall_tree = {}

    for key, value in tree_info.items(): # 봄
            value3 = []
            for v in range(len(value)):
                if lst[key[0]][key[1]] >= value[v]:
                    lst[key[0]][key[1]] -= value[v]
                    value3.append(v+1)
                    value[v] += 1

                    if (key[0], key[1]) not in fall_tree:
                        fall_tree[(key[0], key[1])] = [value[v]]
                    else:
                        fall_tree[(key[0], key[1])].append(value[v])
                else:
                    if v // 2 != 0:
                        if (key[0], key[1]) not in spring_dead_tree:
                            spring_dead_tree[(key[0], key[1])] = [value[v]]
                        else:
                            spring_dead_tree[(key[0], key[1])].append(value[v])
            tree_info[key] = value3[:]

    print(tree_info, cnt)
    for key, value in spring_dead_tree.items():  # 여름
        for v2 in value:
            lst[key[0]][key[1]] += v2 // 2


    for key, value in fall_tree.items():  # 가을

        for v3 in range(len(value)):
            if value[v3] % 5 == 0:
                for w in range(8):
                    di = key[0] + dx[w]
                    dj = key[1] + dy[w]
                    if -1 < di < N and -1 < dj < N:
                        if (di, dj) not in tree_info:
                            tree_info[(di, dj)] = deque()
                            tree_info[(di, dj)].appendleft(1)
                        else:
                            tree_info[(di, dj)].appendleft(1)

    for i in range(N):  # 겨울
        for j in range(N):
            lst[i][j] += winter_info[i][j]

    cnt += 1

    if cnt == K:
        break

result = 0
print(tree_info)
for key, value in tree_info.items():
    result += len(value)

print(result)

