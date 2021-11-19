# Python 3 시간 초과, PyPy3 통과

import sys
from collections import defaultdict
import copy
def input(): return sys.stdin.readline().split()


n, m, k = map(int, input())
winter = [list(map(int, input())) for _ in range(n)]
garden = [[5]*n for _ in range(n)]

dicT = defaultdict(int)  # key: tree age, value: tree count
for i in range(1, 11):
  dicT[i] = 0
trees = [[copy.deepcopy(dicT) for _ in range(n)] for _ in range(n)]

for _ in range(m):
  x, y, tree = map(int, input())
  trees[x-1][y-1][tree] += 1


def spring_summer():
  for i in range(n):
    for j in range(n):
      tmp = copy.deepcopy(dicT)
      flag = False  # True: 나무 사망
      for age, cnt in trees[i][j].items():
        if cnt == 0:
          continue

        elif flag:
          garden[i][j] += int(age / 2) * cnt

        elif age * cnt <= garden[i][j]:
          garden[i][j] -= age * cnt
          tmp[age + 1] += cnt

        elif age * cnt > garden[i][j]:
          able = int(garden[i][j] / age)  # 양분을 먹을 수 있는 나무
          garden[i][j] = garden[i][j] % age
          tmp[age + 1] += able

          unable = cnt - able  # 양분을 먹을 수 없는 나무
          garden[i][j] += int(age / 2) * unable
          flag = True

      trees[i][j] = tmp


def autumn_winter():
  for i in range(n):
    for j in range(n):
      for age, cnt in trees[i][j].items():
        if cnt == 0:
          continue

        elif age % 5 == 0:
          for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
            nx, ny = i + dx, j + dy
            if (0 <= nx < n) and (0 <= ny < n):
              trees[nx][ny][1] += cnt

      garden[i][j] += winter[i][j]  # winter


for _ in range(k):
  spring_summer()
  autumn_winter()


total_tree = 0
for i in range(n):
  for j in range(n):
    for age, cnt in trees[i][j].items():
      total_tree += cnt

print(total_tree)
